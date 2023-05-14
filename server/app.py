from fastapi import FastAPI, UploadFile
from transformers import pipeline
from PIL import Image
import io


app = FastAPI()
pipe = pipeline(task="image-classification", model="skyau/dog-breed-classifier-vit")


@app.get("/")
def root():
    """
    Test function
    :return: greetings
    """
    return {"message": "Сервис для определения породы собакена."}


@app.post("/predict/")
def predict(photo: UploadFile):
    """
    Predicts the breed of a dog from a given photo
    :param photo: UploadFile
    :return: dog breed and prediction probability
    """
    file_bytes = photo.file.read()
    image = Image.open(io.BytesIO(file_bytes))
    predictions = pipe(image)
    first_pred = predictions[0]
    label = first_pred['label']
    score = round(first_pred['score'], 2) * 100
    return {"label": label, "score": score}
