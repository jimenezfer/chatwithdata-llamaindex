# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port for the Streamlit app
EXPOSE 8501

# Set the default command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]
