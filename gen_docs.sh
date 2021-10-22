#!/bin/bash
docker run --rm -v $PWD/app:/usr/src/app python:3.10.0 /bin/bash -c 'cd /usr/src/app && pip install -r pip-requirements.txt && pdocs -ov -o ../docs as_html __main__ ./classes'
