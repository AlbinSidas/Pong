/* 
Hade gärna löst en klass som alla moving targets ärver ifrån
som kan hålla i attribut som x, y, höjd, bredd, speed då alla
dessa attribut är desamma för entities som rör sig på spelbrädet. 
*/
class Player {
    constructor(start_x, start_y, width, height, nickname, speed=1) {
      this.nickname = nickname
      this.x = start_x;
      this.y = start_y;
      this.width = width;
      this.height = height;
      this.speed = speed;
    }
  }
  