
class Ball {
    constructor(startX, startY, boardHeight, boardWidth, width=1, height=1, speed=1) {
        this.x = startX;
        this.y = startY;
        this.width = width;
        this.height = height;
        this.enviroment = boardHeight;
        this.boardHeight = boardHeight;
        this.boardWidth = boardWidth;

        this.speed = this.calculateSpeedPerSecond(8);
        
        // Initialize a random direction which the ball will take by
        // looking at how much the ball will move each update and take
        // a target X away from current position to that target.
        let targetX = Math.floor(Math.random() * this.speed);
        let targetY = Math.floor(Math.random() * this.speed);

        this.directionX = targetX;
        this.directionY = targetY;

    }

    calculateSpeedPerSecond(time){
        /* Time it takes from top to bottom of map in a straight line*/
        let topToBottom = this.enviroment - this.height;
        return Math.ceil(topToBottom / time);
    }
    
    update(timeSinceUpdate) {
      // Calculate time moved since last update
      // Set new X Y
      if (timeSinceUpdate > 1500) {
          return
      }
      
      /* 
      TODO 
      LÖS WINCONDITION
      */
      this.x += this.directionX;
      if (this.x >= this.boardWidth - 1){
        // Wincontdition
        console.log("BALLOUT X HIGHER than X (RIGHT")
        // Bounce steps back into board and update direction
        let bounceDistance = this.x - this.boardWidth;
        this.x = this.boardWidth - bounceDistance;
        
        if (this.x >= this.boardWidth - 1) {
            this.x = this.boardWidth - 1;
        }
        
        this.directionX *= -1;

      } else if (this.x <= 0) {
        console.log("BALLOUT X LOWER 0 (LEFT")
        this.x = Math.abs(this.x)
        this.directionX *= -1;
        
        if (this.x == this.boardWidth) {
          this.x = 1;
        }
      }
      
      
      this.y += this.directionY;
      if (this.y >= this.boardHeight - 1){

        let bounceDistance = this.y - this.boardHeight;
        this.y = this.boardHeight - bounceDistance;
        this.directionY *= -1;

        if (this.y > this.boardHeight - 1) {
          this.y = this.boardHeight - 1;
        }

      } else if (this.y < 0) {

        this.y = Math.abs(this.y)
        this.directionY *= -1;
        if (this.y == this.boardHeight) {
          this.y = 1;
        }
      }
      
      console.log("Time since update: ", timeSinceUpdate);

    }
}

  
module.exports = Ball