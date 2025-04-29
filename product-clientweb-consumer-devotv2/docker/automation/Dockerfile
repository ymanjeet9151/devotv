FROM ubuntu:latest
ARG environment
ARG package_path
ARG execute_path
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_SESSION_TOKEN
ENV environment=${environment} \
    package_path=${package_path} \
    execute_path=${execute_path}
# Set environment variables to prevent prompts during installations
ENV DEBIAN_FRONTEND=noninteractive
# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg \
    software-properties-common \
    unzip \
    && rm -rf /var/lib/apt/lists/*
# Add Google Chrome's repository and install the latest stable version
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable
# Download and install Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome*.deb && \
    apt-get install -f -y && \
    rm google-chrome-stable_current_amd64.deb
# # Download and install chromedriver
RUN wget https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.165/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip && \
    mv chromedriver-linux64/chromedriver /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver && \
    rm -rf chromedriver-linux64.zip chromedriver-linux64
# Add the deadsnakes PPA for Python 3.10
RUN add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update && apt-get install -y python3.10 python3.10-distutils python3.10-venv
# Install pip for Python 3.10
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
# Set Python 3.10 as the default python
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
# Verify installations
RUN python --version && python3 --version && google-chrome --version && chromedriver --version
# # Set an alias for Python 3.10
RUN echo "alias python=python3.10" >> ~/.bashrc
WORKDIR /app
COPY . /app  
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir awscli && \
    aws s3 cp s3://shared-rivittv-automation/${package_path} /app/${package_path} && \
    pip install /app/${package_path}
CMD python ${execute_path} -v stack:headless