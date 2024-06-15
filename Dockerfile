#штука для упаковки нашего приложения

FROM python:3.11-slim

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--post", "80"]