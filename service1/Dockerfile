FROM python:3.7
WORKDIR /service1
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
