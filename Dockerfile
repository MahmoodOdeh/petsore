FROM python:3.12

# Install necessary packages
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg

# Install Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y \
    google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Install Microsoft Edge (Chromium)
RUN wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | apt-key add - \
    && echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge-dev.list \
    && apt-get update && apt-get install -y \
    microsoft-edge-dev \
    && rm -rf /var/lib/apt/lists/*

# Set ChromeDriver version
ENV CHROME_DRIVER_VERSION="92.0.4515.107"

# Download and install ChromeDriver
RUN wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /tmp \
    && mv /tmp/chromedriver /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver


WORKDIR /usr/src/tests

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "--version"]
