
class Ball {
    constructor(startX, startY, boardHeight, boardWidth, width=1, height=1) {
        this.x = startX;
        this.y = startY;
        this.width = width;
        this.height = height;
        this.boardHeight = boardHeight;
        this.boardWidth = boardWidth;

        // Boardheight indicates that it will have a speed of 1
        this.speed = this.calculateSpeedPerSecond(boardHeight);
        
        // Initialize a random direction which the ball will take by
        // looking at how much the ball will move each update and take
        // a target X away from current position to that target.
        this.directionX = Math.floor(Math.random() * this.speed) + 1;
        if (Math.random() > 0.5) {
          this.directionX *= -1;
        }

        this.directionY = Math.floor(Math.random() * this.speed) + 1;
        if (Math.random() > 0.5) {
          this.directionX *= -1;
        }
    }

    calculateSpeedPerSecond(time){
        /* Time it takes from top to bottom of map in a straight line*/
        //let topToBottom = this.boardHeight - this.height;
        return Math.ceil(this.boardHeight / time);
    }

    checkPlayerCollision(players){
        let collision = false;

        /* 
        This could also have easily implemented on which tile of the player it bounces, for example
        if the ball bounces on the top of the player board it gets diected towards the top of the map 
        */
        players.forEach(player => {
            // Check right or left
            if (player.x <= Math.floor(this.boardWidth / 2)){
                // left player
                if (this.x + this.directionX + this.width <= player.x + player.width && this.x + this.width >= player.x + player.width){
                    // Ball is to the left of left player after updating direction

                    // If player is in way of the ball
                    if (player.y <= this.y && player.y + player.height >= this.y){
                        let bounceDistance = Math.abs(this.directionX - (this.x - player.x));
                        this.x = player.x + bounceDistance;
                        this.directionX *= -1;
                        collision = true;
                    }
                  
                }
            } else {
                //right player
                if (this.x + this.directionX + this.width >= player.x && this.x + this.width <= player.x){
                    // Ball is to the left of left player after updating direction

                    // If player is in way of the ball
                    if (player.y <= this.y && player.y + player.height >= this.y){
                      let bounceDistance = Math.abs(this.directionX - (player.x - (this.x + this.width)));
                      this.x = player.x - bounceDistance;
                      this.directionX *= -1;
                      collision = true;
                    }
                }
            }
        })
        
        return collision;
    }
    
    update(timeSinceUpdate, players) {
      // Calculate time moved since last update
      // Set new X Y
      if (timeSinceUpdate > 1500) {
          return
      }
      
      let gameDone = false;
      if (!this.checkPlayerCollision(players)){
        // If no player collision, move the ball and check win condition
        this.x += this.directionX;
        if (this.x >= this.boardWidth - 1){

          this.directionX *= 0;
  
          if (this.x >= this.boardWidth - 1) {
              this.x = this.boardWidth - 1;
          }
          gameDone = true;
  
        } else if (this.x <= 0) {
          
          this.x = 0;
          if (this.x == this.boardWidth) {
            this.x = 0;
          }
          this.directionX *= 0;
          gameDone = true;
        }
        
      }
      
      if (gameDone){
        // Don't move around the ball when tha game is finished
        return
      }

      this.y += this.directionY;
      if (this.y >= this.boardHeight - 1){

        let bounceDistance = this.y - this.boardHeight;
        this.y = this.boardHeight - bounceDistance;
        this.directionY *= -1;

        if (this.y >= this.boardHeight - 1) {
          this.y = this.boardHeight - 1;
        }

        
      } else if (this.y <= 0) {

        this.y = Math.abs(this.y)
        this.directionY *= -1;
        if (this.y == this.boardHeight) {
          this.y = 1;
        }
      } 
    }
}
module.exports = Ball