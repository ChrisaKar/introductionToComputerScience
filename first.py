import random; #exercise1
w, h = 10, 10;
Matrix = [[None for x in range(w)] for y in range(h)]; #creating a 10X10 array
for x in range(10):
 for y in range(10):
  Matrix[x][y]= random.choice(['S','O']); #filling the table randomly with S or O


counter=0; #counter will hold the total number of SOS
for x in range(10):
 for y in range(10):
  if(Matrix[x][y]=='S'):
   if(x>1):
    if(Matrix[x-2][y]=='S' and Matrix[x-1][y]=='O'): #checking for vertical SOS
     counter+=1;
    if(y>1):
     if(Matrix[x-2][y-2]=='S' and Matrix[x-1][y-1]=='O'): #checking for diagonal SOS
      counter +=1;
    if(y<=7):
     if(Matrix[x-2][y+2]=='S' and Matrix[x-1][y+1]=='O'): #checking for diagonal SOS of opposite direction
      counter+=1;
   if(y>1):
    if(Matrix[x][y-2]=='S' and Matrix[x][y-2]=='O'): #checking for horizontal SOS
     counter+=1;


print("Total SOS number: " + str(counter));
print("\nTable:")
for line in Matrix:
    print(*line) 

holdInput = input(); #asking for random input in order for the result to remain printed