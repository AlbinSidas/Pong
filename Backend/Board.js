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
        // This assumes a player might b able to move in right and
        // left manners also
        
        // For each ball, check if player is on either side, else
        // just continue
        this.entities.balls.forEach(ball => {
           this.entities.players.forEach(player => {
              // Check right or left

              /* 
                Kolla om en boll korsar en player i X led

                Då måste jag veta vilken sida spelaren är på

              */
              //console.log(player.x + player.width, ball.x)
              //console.log(player.x + player.width == ball.x - 1);

              if (player.x <= Math.floor(this.boardWidth / 2)){
                  // left player
                  if (ball.x + ball.directionX + ball.width <= player.x + player.width && ball.x + ball.width >= player.x + player.width){
                    // Ball is to the left of left player after updating direction

                    // If player is in way of the ball
                    if (player.y >= ball.y && player.y - player.width <= ball.y){
                        console.log("BOUNCE LEFT")
                        ball.bounce(player.x + player.width)
                    }

                  }
              } else {
                  //right player
                  if (ball.x + ball.directionX >= player.x + player.width && ball.x <= player.x + player.width){
                    // Ball is to the left of left player after updating direction

                    // If player is in way of the ball
                    if (player.y >= ball.y && player.y - player.width <= ball.y){
                        console.log("BOUNCE Right")
                        ball.bounce(player.x)
                    }

                  }
              }
          })
           
        })
    }
  }

  module.exports = Board
