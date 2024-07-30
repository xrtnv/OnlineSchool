FROM python:3.12.4

WORKDIR /lms

COPY requirements.txt /lms/

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
