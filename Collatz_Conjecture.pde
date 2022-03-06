void setup() {

  size(1080, 1080);
  background(0);
  
  for (int i = 1; i < 10000; i++){
  
    //int i = 50;
    IntList sequence = new IntList();
    int n = i;
    
    do {
      sequence.append(n);
      n = collatz(n);
    } 
    while (n != 1);
    
    sequence.append(1);
    sequence.reverse();
    
    float len = 10;
    float angle = (PI)/(12);
   
   resetMatrix();
   translate(0, height/2);
   
   for (int j = 0; j < sequence.size(); j++){
   
     int value = sequence.get(j);
     
     if (value % 2 == 0) {
       rotate(-angle);
     } 
     else {
       rotate(angle);
     }
     
     stroke(255, 50);
     line(0, 0, len, 0);
     translate(len, 0);
     
     }
     
    // Visualize the list
    
  }
  
  //saveFrame("CollatzOutput/collatz_PIby12.png");
  
}

int collatz (int n){

  // even
  if (n % 2 == 0){
    return n / 2;
    
  // odd
  } else {
    return (n * 3 + 1)/2;
  }
  
}
