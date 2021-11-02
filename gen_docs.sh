#!/bin/bash
printf "  Generating documentation within Docker container. . .\n"
printf "=========================================================\n"
docker run --rm -v $PWD/app:/app python:3.10.0 /bin/bash -c 'cd ./app/ ; pip install -r ./pip-requirements.txt ; rm -r ./docs_temp/ ; pdoc --logo https://placedog.net/300?random -d google -o./docs_temp ../app ./blueprints/ ./errors/ ./forms/ ./models/ ./security/ ./testing/'

printf "  Removing docs folder, if it exists. . .\n"
printf "===========================================\n"
rm -v -r ./docs/

printf "  Recreating docs folder. . .\n"
printf "===============================\n"
mkdir -v ./docs/

printf "  Moving docs from app/docs_temp/ folder into docs/ folder. . .\n"
printf "=================================================================\n"
mv -v ./app/docs_temp/* ./docs/

printf "  Removing app/docs_temp folder. . .\n"
printf "======================================\n"
rm -v -r ./app/docs_temp/
