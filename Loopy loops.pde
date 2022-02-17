static final int NUM_LINES = 10;

float a = 10;
float b = 0.05;
float c = 250;
float d = 0.1;
float f = 0.1;

float x1(float t){
  return ((sin(a*t)/b)+c) * cos(t);
}

float y1(float t){
  return ((sin(a*t)/b)+c) * sin(t);
}

float x2(float t){
  return ((sin(a*(t))/b)+c) * cos(t-d);
}

float y2(float t){
  return ((sin(a*(t))/b)+c) * sin(t-d);
}

float x3(float t){
  return ((sin(a*(t))/b)+c) * cos(t-(d+f));
}

float y3(float t){
  return ((sin(a*(t))/b)+c) * sin(t-(d+f));
}

float t;

void setup(){
  background(20);
  size(600, 600);
}

void draw() {
  background(#090421);
  strokeWeight(2);
  
  translate(width/2, height/2);
  stroke(255);
  
  //for (int i=0; i < NUM_LINES; i++){
    
  //  if(i%10 == 0){
  //    stroke(#590d22);
  //  }
  //  else if(i%10 == 1){
  //    stroke(#800f2f);
  //  }
  //  else if(i%10 == 2){
  //    stroke(#a4133c);
  //  }
  //  else if(i%10 == 3){
  //    stroke(#c9184a);
  //  }
  //  else if(i%10 == 4){
  //    stroke(#ff4d6d);
  //  }
  //  else if(i%10 == 5){
  //    stroke(#ff758f);
  //  }
  //  else if(i%10 == 6){
  //    stroke(#ff8fa3);
  //  }
  //  else if(i%10 == 7){
  //    stroke(#ffb3c1);
  //  }
  //  else if(i%10 == 8){
  //    stroke(#ffccd5);
  //  }
  //  else if(i%10 == 9){
  //    stroke(#fff0f3);
  //  }
    
  //line(x1(t + i), y1(t + i), x2(t + i), y2(t + i));
  //}
  
  line (x1(t), y1(t), x2(t), y2(t));
  line (x2(t), y2(t), x3(t), y3(t));
  
  t += 0.005;
  
  //saveFrame("vintOutput2/vintage_####.png");
}
