FROM python:alpine3.10

WORKDIR /data

COPY requirements.txt .
RUN \
apk add --no-cache postgresql-libs && \
apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
python3 -m pip install -r requirements.txt --no-cache-dir && \
apk --purge del .build-deps


ENTRYPOINT ["python","/data/web.py"]
# docker run  --rm -it --name postgres_app  --mount type=bind,src=/srv/app,dst=/data  -p=9012:80 python_app

