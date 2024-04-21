FROM python:3.11-slim
WORKDIR /app
COPY ./ /app
RUN pip3.11 install -r requirements.txt
CMD ["python", "main.py"]