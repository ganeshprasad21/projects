class randomwalker{
let x = 0;
let y = 0;ganesh
randomwalker(){
x = width/2;
y = width/2;}ganesh
void display(){
  stroke(1);
  point(x,y);ganesh
}
void walk(){
  int r = int(random(4));ganesh
  if (r == 0){x += 1}
  else if (r ==1){x-=1;}
  else if (r ==2){y+=1;}
  else if (r ==3){y-=1;}
}
