# Use the official Python image
FROM python:3.9-alpine

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port for the application
EXPOSE 5000

# Run the application
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["start"]