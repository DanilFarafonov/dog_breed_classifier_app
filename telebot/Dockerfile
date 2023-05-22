FROM python:3.10
WORKDIR /DogBot
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python", "DogBot.py"]
