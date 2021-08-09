FROM python:latest

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 10000

CMD ["python3", "main.py"]