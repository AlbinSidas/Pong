
class Ball {
    constructor(start_x, start_y, width=1, height=1, speed=1) {
        this.x = start_x;
        this.y = start_y;
        this.width = width;
        this.height = height;
        this.enviroment = 40
        this.speed = this.calculateSpeedPerSecond(1.2);

    }

    calculateSpeedPerSecond(time){
        /* Time it takes from top to bottom of map */
        let topToBottom = this.enviroment - this.height;
        return Math.ceil(topToBottom / time);
    }
    
    move(timeSinceUpdate) {
      // Calculate time moved since last update
      // Set new X Y

    }
}

  
module.exports = Ball