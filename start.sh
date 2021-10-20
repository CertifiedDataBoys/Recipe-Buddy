echo "Starting Docker for Recipe Buddy..."
docker-compose up --build 2>&1 | tee "docker.log"
echo "\nExiting..."
