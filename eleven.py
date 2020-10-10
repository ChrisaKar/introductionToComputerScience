import random; #exercise11
import math;

r2 = random.randint(1, 1000); #finding a random number between 1 and 1000 except from 196 and 879 
while(r2==196 or r2==879): 
 r2 = random.randint(1, 1000);

counter = 0; #holds the number of additions
print("Random number created: " + str(r2)); #prints the original number
resultFound=False;
while(not resultFound): #ends when the result is found
 r=r2; #r2 keeps the previous result while r changes in order to reverse the original number
 reverse=0; #keeps the reverse number
 while(r!=0):
  division= r%10*pow(10, int(math.log10(r))); #finds the modulo of the number with 10 and adds the decimal digits needed
  r=int(r/10); 
  reverse+=division;
 
 if(reverse==r2): #if the number equals the reversed, the goal is reached
  resultFound=True;
 else: 
  r2+=reverse; #otherwise the reversed num is added and the process continues
  counter+=1;
 
print("Number of additions: "+ str(counter));
terminalInput=input(); 