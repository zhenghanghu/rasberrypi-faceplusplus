// Sweep

// by BARRAGAN <http://barraganstudio.com> 

// This example code is in the public domain.





#include <Servo.h> 

 

Servo myservo;  // create servo object to control a servo 

                // a maximum of eight servo objects can be created 

 

int pos = 0;    // variable to store the servo position 

char input; 

 

void setup() 

{ 

  myservo.attach(9);  // attaches the servo on pin 9 to the servo object 

  Serial.begin(9600);

} 

 

 

void loop() 

{ 

  if(Serial.available()>0){

    input = Serial.read();

  }

  if(input == 'A'){

    myservo.write(120);

    delay(5000);

    //myservo.write(30);

    input ='B';

  }

  if(input == 'B'){

    myservo.write(10);

  }

} 
