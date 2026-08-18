FROM python:3.11-slim
WORKDIR /app
COPY chat_llama/requirements.txt .
RUN pip install -r requirements.txt
COPY chat_llama/ .
ENV FLASK_APP=app.py
EXPOSE 8080
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
