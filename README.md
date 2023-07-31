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
