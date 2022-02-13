import peasy.*;

float x = 0.01; float y = 0; float z = 0;
float a = 10; float b = 28; float c = 8.0/3.0;

ArrayList<PVector> points = new ArrayList<PVector>();

PeasyCam cam;

void setup(){
  size(800, 600, P3D);
  colorMode(HSB);
  cam = new PeasyCam(this, 500);
}

void draw(){
  background(0);
  
  // Differential equations
  float dt = 0.01; 
  float dx = (a*(y-x))*dt; float dy = (x*(b-z)-y)*dt; float dz = (x*y-c*z)*dt;
  
  x = x+dx;
  y = y+dy;
  z = z+dz;
  
  points.add(new PVector(x, y, z)); // Adding the new point into the ArrayList
  
  translate(0, 0, -80);
  //rotateX(90);
  //rotateY(-90);
  //rotateZ(180);
  scale(5);
  stroke(255);
  strokeWeight(0.4);
  noFill();
  
  float hu = 0;
  int count = 0;
  beginShape();
  for (PVector v : points){
    stroke(hu, 255, 200);
    vertex(v.x, v.y, v.z);
    // Plotting x, y, z of every vector v in points with a for loop
    // You need to plot it repeatedly because of the background(0); at start
    
    hu += 0.05;
    count += 1;
    
    rotateX((hu)/(hu*360));
    println(count*((hu)/(hu*360)))
    //rotateY((hu)/(hu*360));
    //rotateZ((hu)/(hu*360));
    
    
    if(hu > 255){
      hu = 0;
    }
  }
  endShape();
  
  //saveFrame("lorenzOutput2/lorenzAtt_####.png");
}  
