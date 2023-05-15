FROM python:3.10
WORKDIR /app
EXPOSE 8000
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY app.py .
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]