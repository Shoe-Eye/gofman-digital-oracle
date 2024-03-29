import torch
import sys
import os

from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig

path = os.path.abspath(".")
sys.path.append(path)

from conversation import Conversation, generate

LLM_MODEL_NAME = "cwiz/llama-saiga-7b-gofman"
TTS_MODEL_PATH = "tts/model.pth"

from TTS.api import TTS

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
generation_config.max_new_tokens = 800

inputs = [
    "Какое печенье любите?",
    "Что случилось в херсоне?",
    "Что с вашими усами?",
]
for i, inp in enumerate(inputs):
    conversation = Conversation()
    conversation.add_user_message(inp)
    prompt = conversation.get_prompt(tokenizer)

    output = generate(model, tokenizer, prompt, generation_config)

    tts.tts_to_file(text=output, file_path=str(i) + ".wav")

    print(inp)
    print(output)
    print()
    print("==============================")
    print()
