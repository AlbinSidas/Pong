/* 
Hade gärna löst en klass som alla moving targets ärver ifrån
som kan hålla i attribut som x, y, höjd, bredd, speed då alla
dessa attribut är desamma för entities som rör sig på spelbrädet. 
*/
class Player {
    constructor(start_x, start_y, id, side, speed=1, width=1, height=4) {
      this.x = start_x;
      this.y = start_y;
      this.width = width;
      this.height = height;
      this.id = id;
      this.speed = speed;
    }
  }
  
module.exports = Player
