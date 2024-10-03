## TicTacToe application
### Python/FastAPI application
Please note that this is not to be used for production use. FastAPI is used being a light weight framework for a simple API implementation.

### Description
- There is no human input. Both player moves are simulated
-  Moves will be determined using an external service, [Random API](https://github.com/brendanmaguire/random) (this service should be run locally; there is no deployed version to query)
-  The game will stop as soon as there is a winner or reaching game over
-  The winner and cells of the boards will be returned using [TicTacToe API](http://localhost:8000/tictactoe-round)


Project structure:
```
├── compose.yaml
├── Dockerfile
├── requirements.txt
├── app
    ├── __init__.py
    ├── main.py
    ├── services.py
    ├── models
        ├── boards.py
        ├── players.py
        ├── tictactoe.py
    ├── tests
        ├── test_boards.py
        ├── test_players.py
        ├── test_services.py
        ├── test_tictactoe.py
```

## Deploy with docker compose

```shell
docker-compose up -d --build
```
## Expected result

Listing containers must show one container running and the port mapping as below:
```
$ docker ps
CONTAINER ID   IMAGE          COMMAND       CREATED              STATUS              PORTS                                               NAMES
7087a6e79610   5c1778a60cf8   "/start.sh"   About a minute ago   Up About a minute   80/tcp, 0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   fastapi-application
```

After the application starts, navigate to `http://localhost:8000` in your web browser and you should see the following json response:
```
{
"message": "OK"
}
```

Stop and remove the containers
```
$ docker compose down
```

Run tests
```
$ docker-compose run api  pytest
```

While the application is running, to access the API documentation, navigate to `http://localhost:8000/docs`

### Next Steps
- Add Git setup
- Add test cases specially for the API and models initialization corner cases
- Setup environment variables configuration file .env
- For development, setup a docker volume to sync code changes between the host machine and the container
- Better error handeling with custom ones to differentiate between different causes. Add more human friendly messages
- Add linter ex: flake
- Add poetry setup
