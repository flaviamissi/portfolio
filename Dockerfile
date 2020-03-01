FROM python:3.8-alpine3.11

WORKDIR /app

RUN apk add --update gcc musl-dev

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["env", "FLASK_APP=api.py", "flask", "run"]
