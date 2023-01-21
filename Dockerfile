FROM python:3.9-alpine

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

RUN apk add --no-cache curl
RUN curl -fsSL -o /usr/local/bin/dbmate https://github.com/amacneil/dbmate/releases/latest/download/dbmate-linux-amd64 && chmod +x /usr/local/bin/dbmate 

WORKDIR /app

EXPOSE 8000

ENTRYPOINT [ "sh", "./scripts/entrypoint.sh"]
CMD ["start"]