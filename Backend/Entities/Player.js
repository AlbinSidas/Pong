/* 
Hade gärna löst en klass som alla moving targets ärver ifrån
som kan hålla i attribut som x, y, höjd, bredd, speed då alla
dessa attribut är desamma för entities som rör sig på spelbrädet. 
*/
class Player {
    constructor(start_x, start_y, id, enviroment=40, width=1, height=4) {
        this.x = start_x;
        this.y = start_y;
        this.width = width;
        this.height = height;
        this.id = id;

        // Speed is implicitly tiles per second
        this.speed = this.calculateSpeedPerSecond(2)
    }

    calculateSpeedPerSecond(time){
        /* Time it takes from top to bottom of map */
        let topToBottom = this.enviroment - this.height;
        return Math.ceil(topToBottom / time);
    }

    update(timeSinceUpdate, action) {
      console.log("Update player")
      if (timeSinceUpdate > 1500) {
          return
      }
      
      let secondsSinceUpdate = timeSinceUpdate * 1000
      let tilesToMove = this.speed * secondsSinceUpdate;

      switch(action) {
        case "up":
          console.log("UPP")
          this.y += tilesToMove;
          
          break;
        case "down":
          console.log("NER")
          this.y -= tilesToMove;
          break;
        /*
        case "right":
            // code block
            break;
        case "left":
          // code block
          break;
        */
        default:
          // No action
      }
      
    }

}
  
module.exports = Player
