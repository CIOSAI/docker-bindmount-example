# syntax=docker/dockerfile:1

FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5379

CMD [ "python", "./app.py" ]