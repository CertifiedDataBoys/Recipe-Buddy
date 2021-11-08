# User official python base image
FROM python:3.10.0

# Set our container's working directory to /app
WORKDIR /app

# Copy pip-requirements.txt into the root of our container's working directory
COPY pip-requirements.txt ./
# Pip install from pip-requirements.txt
RUN pip install --no-cache-dir -r pip-requirements.txt

# Copy all project files to our container's working directory
COPY . .

# Wait for DB to be ready
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

# Set the default start command of the container (wait for database and run our application)
CMD sh -c "/wait && flask run --host=0.0.0.0"
