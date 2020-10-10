import random; #exercise6
fourInARow = False; #holds whether there are 4 zeros or ones
counter=0; #holds how many numbers were created
while fourInARow==False: #the process is repeated untill there are 4 in a row
 w, h = 10, 10;
 Matrix = [[None for x in range(w)] for y in range(h)]; #creating 10X10 array with empty values
 over = False;
 for x in range(10):
  for y in range(10):
   Matrix[x][y]= random.choice([1, 0]);
   counter+=1;
   if(x-3>=0):
    if(Matrix[x-3][y]==Matrix[x][y] and Matrix[x-2][y]==Matrix[x][y] and Matrix[x-1][y]==Matrix[x][y]): #checking for vertical numbers in a row
     fourInARow=True; 
     break; #breaks the inner loop since the goal was reached
    if(y-3>=0):
     if(Matrix[x-3][y-3]==Matrix[x][y] and Matrix[x-2][y-2]==Matrix[x][y] and Matrix[x-1][y-1]==Matrix[x][y]): #checking for diagonal numbers in a row
      fourInARow=True;
      break;
   if(y-3>=0):
    if(Matrix[x][y-3]==Matrix[x][y] and Matrix[x][y-2]==Matrix[x][y] and Matrix[x][y-1]==Matrix[x][y]): #checking for horizontal numbers in a row
     fourInARow=True;
     break;
   if(x-3>=0 and y+3<=9):
    if(Matrix[x-3][y+3]==Matrix[x][y] and Matrix[x-2][y+2]==Matrix[x][y] and Matrix[x-1][y+1]==Matrix[x][y]): #checking for diagonal of opposite direction numbers in a row
     fourInARow=True;
     break;     
  if(fourInARow):
   break; #breaks the outer for loop

print("Numbers created: " + str(counter));
print("\nTable:")
for line in Matrix:
    print(*line);
x=input();