FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    libldap2-dev \
    libsasl2-dev \
    python3-pip \
    python3-dev

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY app.py .

CMD ["python3", "app.py"]