[![Tests](https://github.com/lisxen/dog_breed_classifier_app/actions/workflows/python-app.yml/badge.svg)](https://github.com/lisxen/dog_breed_classifier_app/actions/workflows/python-app.yml)

# Телеграм бот для определения породы собаки по фото
Бот был разработан в рамках выполнения студенческого проекта по дисциплине "Программная инженерия". Для упрощения разработки бот-приложение было разделено на два сервиса: 
 - сервис `server` написан на FastAPI и отвечает за распознавание пород при помощи модели машинного обучения [skyau/dog-breed-classifier-vit](https://huggingface.co/skyau/dog-breed-classifier-vit);
 - сервис `telebot` написан с использованием библиотеки pyTelegramBotAPI. 

## Пример работы приложения
![Пример работы приложения](example.gif)
