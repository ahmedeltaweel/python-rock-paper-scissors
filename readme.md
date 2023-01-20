Rock, Paper, Scissors API
This is an API for a two-player game of rock, paper, scissors.

Requirements
Python 3.9 or later
Docker and Docker Compose (if you want to run the application using Docker)
psycopg2 (if you want to run the application using postgres)
Running the Application
Option 1: Using Python
Install the required packages by running pip install -r requirements.txt
Start the application by running python app.py
The application will be running at http://localhost:5000
Option 2: Using Docker
Build the images by running docker-compose build
Start the application and the Postgres database by running docker-compose up
The application will be running at http://localhost:5000
API Endpoints
POST /start: Start a new game. The request body should include the names of the two players in JSON format.
POST /play: Play a turn. The request body should include the choices of the two players in JSON format.
GET /score: Get the current score.
Game State
You can use the psycopg2 library to interact with a Postgres database and save the game state.
You can retrieve the game state from the database and display it to the user by running SELECT statement on the game table.

Example
The following example shows how to start a new game with player1 as Alice and player2 as Bob

```sh
curl -X POST -H "Content-Type: application/json" -d '{"player1":"Alice","player2":"Bob"}' http://localhost:5000/start
```