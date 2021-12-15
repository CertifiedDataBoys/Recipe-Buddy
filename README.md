# Recipe Buddy

## Certified Data Boys

Welcome to the Git repo for Recipe Buddy!


## How to Install Docker
Install Docker following [Docker's guide](https://docs.docker.com/get-docker/) for your operating system.
- Windows Users: [Windows Install](https://docs.docker.com/desktop/windows/install/)
- macOS Users: [Mac Install](https://docs.docker.com/desktop/mac/install/)
- Linux Users: Simply `curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh` or follow the [Linux Install](https://docs.docker.com/engine/install/#server)

## How to install docker-compose
Comes by default Docker installation on Windows and macOS. Linux users [follow this guide](https://docs.docker.com/compose/install/#install-compose-on-linux-systems).

## How to Setup Recipe Buddy
On first run, create a `.env` file in the same directory as `docker-compose.yml` with the following values:
```
SECRET_KEY=MySecretKey
MARIADB_DATABASE=recipebuddy
MARIADB_USER=recipebuddy
MARIADB_PASSWORD=recipebuddy
PASSWORD_SALT=MyPasswordSalt
```
Ensure that you substitute these variables for your own secure variables and do not change them after the database has been created. The database name, username and password are all arbitrary and shouldn't matter. By default, Docker secures your MariaDB installation so as long as the user does not port forward it using Docker, MariaDB is inaccessable to all applications besides the Recipe Buddy application itself.

## How to Run Recipe Buddy
To start the Recipe Buddy application, ensure Docker is running and docker-compose is installed, then:
```bash
docker-compose up -d
```
This will start Recipe Buddy in daemon (background) mode.

To stop Recipe Buddy, run:
```bash
docker-compose down
```

To view the logs of Recipe Buddy, run:
```bash
docker-compose logs -f
```
