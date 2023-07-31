FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel
WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y wget
RUN mkdir tts && cd tts && wget https://huggingface.co/cwiz/igor-gofman-vits-tts/raw/main/config.json && wget https://huggingface.co/cwiz/igor-gofman-vits-tts/resolve/main/model.pth
RUN apt-get install -y espeak
RUN pip install bitsandbytes
COPY bot.py ./bot.py
COPY conversation.py ./conversation.py
VOLUME /root/.cache/torch/sentence_transformers

CMD ["python", "bot.py"]