FROM python:3.11-slim
WORKDIR /app
COPY ./ /app
RUN pip3.11 install -r requirements.txt
EXPOSE 1290
CMD ["python", "main.py"]