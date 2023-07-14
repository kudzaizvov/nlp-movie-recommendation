FROM python:3.10-slim-buster

WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
# Copy all the relevent files from source directory
COPY movies.txt movies.txt
COPY watch_next.py /app/watch_next.py

CMD ["python", "watch_next.py"]