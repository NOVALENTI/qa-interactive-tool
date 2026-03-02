# 1. Use the official Microsoft Playwright image (includes Python and Browsers)
FROM mcr.microsoft.com/playwright/python:v1.58.0-jammy

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy only the requirements first (to optimize build speed)
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the project code
COPY . .

# 6. Ensure Python can find your 'src' folder
ENV PYTHONPATH=/app

# 7. The entry point: This makes the container act like a command-line tool
ENTRYPOINT ["python", "main.py"]