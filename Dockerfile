# Use an official Python runtime as a parent image
FROM python:3.9

# Install necessary dependencies
RUN apt-get update && apt-get install -y wget

# Set the working directory inside the container
WORKDIR /app

# Copy your project files into the container
COPY . /app

# Run Poetry to set up your project and install dependencies
RUN poetry config virtualenvs.create false && \
    poetry install

# # Create and activate a virtual environment
# RUN python -m venv venv
# RUN . venv/bin/activate

# Install project dependencies
#RUN pip install -r requirements.txt

# Install Google Chrome (change this depending on your Docker base image)
RUN apt -f install -y
RUN apt-get install -y wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install ./google-chrome-stable_current_amd64.deb -y
# Run your Selenium tests and generate the HTML report
CMD poetry run pytest
