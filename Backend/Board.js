const Player = require('./Entities/Player');
const Ball = require('./Entities/Ball');

class Board {
    constructor(x, y) {
      // Use these to check boundries
      this.boardWidth = x;
      this.boardHeight = y;
      this.tileSize = 10;

      // Entities
      this.gameBoard = this.initializeGameboard();
      
      // entities
      this.entities = {
          'players' :[],
          'balls'   :[]
      }

      this.initializeBall();
    }
   
    initializeGameboard() {
        // Initialize based on incoming parameters
        let gameBoard = new Array(this.boardHeight).fill(0)
        for (var row in gameBoard) {
            gameBoard[row] = new Array(this.boardWidth).fill(0)
        }
        return gameBoard;
    }

    initializePlayer(id){
        // If there is no connected players, first is connecting
        // and is assigned the furthest left, else to the furthest right.
        if (this.entities.players.length == 2){
            return false;
        }
        
        // Also moving them in one step to not be within walls
        let startX = this.entities.players.length == 0 ? 1 : this.boardWidth - 2;
        let startY = Math.floor(this.boardHeight / 2);
        let player = new Player(startX, startY, id);        
        this.entities.players.push(player);
        
        return true;
    }

    initializeBall(){
        /* Initialize ball to middle of the board */
        let startY = Math.floor(this.boardHeight / 2);
        let startX = Math.floor(this.boardWidth / 2);
        let ball = new Ball(startX, startY, this.boardHeight, this.boardWidth)
        this.entities.balls.push(ball);
    }

    collisionCheck(){
        // Använd denna i move och när updateringar ska göras
    }

    controlEntities(){
        this.entities.players.forEach(player =>{
            // Handles if player tries to go outside world
            if (player.y - player.height > this.boardHeight) {
                player.y = this.boardHeight;
            }
            else if(player.y < 0){
                player.y = 0
            }
        })

        this.entities.balls.forEach(ball => {
          if (ball.y - ball.height > this.boardHeight) {
            ball.y = this.boardHeight;
            /*
            Ändra direction baserat på vad den träffar
            ball.changeDirection();
            */
          } else if (ball.y < 0){
            ball.y = 0;
            /*
            Ändra direction baserat på vad den träffar
            ball.changeDirection();
            */
          } else if (ball.x < 0) {
              for(var i ; i < 10; i++){
                  console.log("Right player won!")
              }
          } else if (ball.x > this.boardWidth) {
              for(var i ; i < 10; i++){
                console.log("Left player won!")

              }  
          }

        })
    }
  
    updateTick(){
        console.log("TICK")
    }
  }

  module.exports = Board
