
class Ball {
    constructor(start_x, start_y, target, width=1, height=1, speed=1) {
        this.x = start_x;
        this.y = start_y;
        this.width = width;
        this.height = height;
        this.enviroment = 40;
        this.current_target = target;
        this.speed = this.calculateSpeedPerSecond(1.2);

    }

    calculateSpeedPerSecond(time){
        /* Time it takes from top to bottom of map */
        let topToBottom = this.enviroment - this.height;
        return Math.ceil(topToBottom / time);
    }
    
    update(timeSinceUpdate) {
      // Calculate time moved since last update
      // Set new X Y
      
      //calculate closes path to current target
      // calcylate the hypotenuse path between 
      console.log("TARGET", this.current_target)
      console.log("POSITION", [this.x, this.y])
      
      // Calculate Hypotenuse by : for each element in sorted order:
      // multiply each element and root it
      /* 
      Typ gör en vanlig i loop som går igenom värden x -> target  X
      y -> target y
      ta ut nästa steg för att komma närmare fårn nuvarandepunk=?
      */
      console.log("Time since update: ", timeSinceUpdate);

    }
}

  
module.exports = Ball