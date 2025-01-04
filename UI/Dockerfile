FROM python:3.9

RUN apt-get update && apt-get install -y python3-pip \
    python3-tk \
    x11-apps

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]