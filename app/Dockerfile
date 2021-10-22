# User official python base image
FROM python:3.10.0

# Set our container's working directory to /usr/src/app
WORKDIR /usr/src/app

# Copy pip-requirements.txt into the root of our container's working directory
COPY pip-requirements.txt ./
# Pip install from pip-requirements.txt
RUN pip install --no-cache-dir -r pip-requirements.txt

# Copy all project files to our container's working directory
COPY . .

# Set the default start command of the container (to run our application)
CMD [ "python", "." ]
