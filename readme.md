# Rock, Paper, Scissors API
This is an API for a two-player game of rock, paper, scissors.

## Requirements
1. Python 3.9 or later
2. Docker and Docker Compose
3. psycopg2
4. dbmate

## Running the Application
### Option 1: Using Python
Install the required packages by running 
```sh
$ pip install -r requirements.txt
```
Start the application by running python app.py
The application will be running at http://localhost:5000

### Option 2: Using Docker
Build the images by running docker-compose build
Start the application and the Postgres database by running docker-compose up
The application will be running at http://localhost:5000

Example
The following example shows how to start a new game with player1 as Alice and player2 as Bob

```sh
curl -X POST -H "Content-Type: application/json" -d '{"player1":"Alice","player2":"Bob"}' http://localhost:5000/game
```