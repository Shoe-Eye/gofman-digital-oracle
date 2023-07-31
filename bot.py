import telebot
import torch
import sys
import os
import uuid

from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig
from TTS.api import TTS

path = os.path.abspath(".")
sys.path.append(path)

from conversation import Conversation, generate

LLM_MODEL_NAME = "cwiz/llama-saiga-7b-gofman"
TTS_MODEL_PATH = "tts/model.pth"


bot = telebot.TeleBot(os.environ.get("BOT_TOKEN"))

tts = TTS(
    model_path=TTS_MODEL_PATH,
    config_path="tts/config.json",
    progress_bar=False,
    gpu=False,
)

config = PeftConfig.from_pretrained(LLM_MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    config.base_model_name_or_path,
    load_in_8bit=True,
    torch_dtype=torch.float16,
    device_map="auto",
)
model = PeftModel.from_pretrained(model, LLM_MODEL_NAME, torch_dtype=torch.float16)
model.eval()

tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL_NAME, use_fast=False)
generation_config = GenerationConfig.from_pretrained(LLM_MODEL_NAME)
generation_config.max_new_tokens = 400


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_chat_action(message.chat.id, "record_audio", timeout=100)

    conversation = Conversation()
    conversation.add_user_message(message.text)
    prompt = conversation.get_prompt(tokenizer)

    output = generate(model, tokenizer, prompt, generation_config)

    id = uuid.uuid4()
    file_path = "./output/" + str(id) + ".wav"
    tts.tts_to_file(text=output, file_path=file_path)
    bot.send_chat_action(message.chat.id, "record_audio", timeout=100)
    voice = open(file_path, "rb")
    bot.send_voice(chat_id=message.chat.id, reply_to_message_id=message.id, voice=voice)
    bot.send_voice(message.chat.id, "FILEID")


bot.infinity_polling()
