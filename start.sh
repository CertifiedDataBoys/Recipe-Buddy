printf "Starting Docker for Recipe Buddy..."
docker-compose up --build 2>&1 | tee "./data/docker.log"
printf "\nExiting...\n"
