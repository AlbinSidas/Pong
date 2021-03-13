/* 
Hade gärna löst en klass som alla moving targets ärver ifrån
som kan hålla i attribut som x, y, höjd, bredd, speed då alla
dessa attribut är desamma för entities som rör sig på spelbrädet. 
*/
class Player {
    constructor(start_x, start_y, id, enviroment, width=1, height=5) {
        this.x = start_x;
        this.y = start_y;
        this.width = width;
        this.height = height;
        this.id = id;
        this.enviroment = enviroment;

        // Speed is implicitly tiles per second
        this.speed = this.calculateSpeedPerSecond(12)
    }

    calculateSpeedPerSecond(time){
        /* Time it takes from top to bottom of map */
        let topToBottom = this.enviroment - this.height;
        return Math.ceil(topToBottom / time);
    }

    update(timeSinceUpdate, action) {
      if (timeSinceUpdate > 1500) {
          return
      }
      
      //let secondsSinceUpdate = timeSinceUpdate * 1000;
      //let tilesToMove = this.speed * secondsSinceUpdate;

      switch(action) {
        case "up":
          this.y -= this.speed;
          if (this.y < 0){
              this.y = 0;
          }
          break;
        case "down":
          this.y += this.speed;
          if (this.y > this.enviroment - this.height) {
            this.y = this.enviroment - this.height;
        }
          break;
        /* If preffered right and left cna be added here*/
        default:
          // No action
      }
      
    }

}
  
module.exports = Player