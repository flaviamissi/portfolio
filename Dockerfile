FROM python:3.8-alpine3.11

WORKDIR /app

RUN apk add --update gcc musl-dev

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["env", "FLASK_APP=api", "flask", "run", "--host", "0.0.0.0"]
