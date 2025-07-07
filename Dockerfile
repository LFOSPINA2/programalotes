FROM python:3.10-slim

WORKDIR /home/user

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    zip \
    unzip \
    openjdk-11-jdk \
    python3-pip \
    python3-dev \
    libffi-dev \
    libssl-dev \
    libsqlite3-dev \
    libbz2-dev \
    libreadline-dev \
    liblzma-dev \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libxml2-dev \
    libxslt1-dev \
    curl && \
    apt-get clean

RUN pip install --upgrade pip setuptools Cython && \
    pip install buildozer openpyxl google-api-python-client oauth2client pyopenssl certifi requests

COPY . .

CMD ["buildozer", "android", "debug"]