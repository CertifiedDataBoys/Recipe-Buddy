#!/bin/bash
docker run --rm -v $PWD/app:/app python:3.10.0 /bin/bash -c 'cd /app && pip install -r pip-requirements.txt && pdocs -ov -o ../docs as_html __main__ ./classes'
