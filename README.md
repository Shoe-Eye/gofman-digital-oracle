# gofman-digital-oracle

Igor Goffman's Digitized Consciousness of Most Smarted Man in Ukraine

## Datasets

- [igor-gofman-text](https://huggingface.co/datasets/cwiz/igor-gofman-text/tree/main)
- [igor-gofman-tts](https://huggingface.co/datasets/cwiz/igor-gofman-tts)

## Models

- [LLaMa-Saiga-7b-Gofman](https://huggingface.co/cwiz/llama-saiga-7b-gofman) Siaga-7B finetuned on gofman texts
- [igor-gofman-vits-tts](https://huggingface.co/cwiz/igor-gofman-vits-tts) [Coqui-TTS](https://github.com/coqui-ai/TTS) VITS weights trained from igor-gofman-tts

## Reproducing Results

LLM funetuning performed with [text-generation-webui](https://github.com/oobabooga/text-generation-webui) on concatenated text dataset on Gofman-Text dataset. Saiga weights were merged with LLaMa, hence LoRA performed twice.

## Scripts

- [generate.py](generate.py) - huggingface example of LLaMa-Saiga-7b-Gofman invocation
- [bot.py](bot.py) - run generate.py model as telegram bot

## Useful Resources

* [so-vits-svc-5.0](https://github.com/PlayVoice/so-vits-svc-5.0) voice-to-voice model (transfers the style for vocals/speech)
* [Coqui TTS VITS](https://github.com/coqui-ai/TTS/tree/dev/recipes/thorsten_DE/vits_tts) voice-to-text model (excels at intonation but struggles with longer sentences and unseen words)
* [bark](https://github.com/suno-ai/bark) SOTA text-2-voice model for voice-2-voice
* [Saiga](https://huggingface.co/IlyaGusev/saiga_7b_lora) LLaMa finetuned for Russian text
