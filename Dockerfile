#syntax=docker/dockerfile:1
FROM python:3.10-slim-buster

WORKDIR /app

COPY app.py app.py

CMD ["python3", "app.py"]
RUN mkdir /app/images

# пример запуска:

# docker run --name favicon --mount type=volume,src=favicon,dst=/app/images/ favicon_thrief
# сохряняет фавиконы в вольюм на хосте 
