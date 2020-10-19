from matplotlib import pyplot as plt; #exercise2
fileNotFound = False;
while not fileNotFound:
 try:
  path= input("please insert the text file's path: "); #the file path
  f = open(path,"r"); #opens the file in read mode
  file = f.read(); #saves the text files context in the file variable
  fileNotFound=True;
 except:
  print("File not found \n");
  
letters = [char for char in file]; #divides text to an array of characters
final_letters =[]; #holds the letters
letterCounter=[]; #holds how many times each character appeared


for x in range(len(letters)):
 found = False;
 for y in range(len(final_letters)):
  if(letters[x].lower()== final_letters[y].lower()):
   letterCounter[y]+=1; #adds to the position of the letter
   found =True;
   break;
 if(not(found) and letters[x]!=" "): #adds new letters to the list
   letterCounter.append(1); 
   final_letters.append(letters[x].lower());


fig = plt.figure(figsize = (10, 5)); 
plt.bar(final_letters, letterCounter, color ='maroon', width = 0.4); #diagram's info
plt.xlabel("Letters");
plt.ylabel("Number of times appeared");
plt.title("Statistics");
plt.show(); #diagram is shown
