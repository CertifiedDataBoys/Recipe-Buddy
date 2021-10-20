FROM python:3.10.0

WORKDIR /usr/src/app

COPY pip-requirements.txt ./
RUN pip install --no-cache-dir -r pip-requirements.txt

COPY . .

CMD [ "python", "./app.py" ]
