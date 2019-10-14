#1)Write a program to find a longest substring without repeating characters from a given string input from the console.
#Sample Input: ‘ababcdxa’
#Sample Output: abcdx


#to get the word from the consol
string = str(input('enter your string'))
#to calculate lenght of the word
n = len(string)
#define a variable that store the final word without replication
newword=''
word = {} 
#to assign values of number of occurance of the first letter
word[string[0]] = 0 
#search for the occurance of the letter
for i in range(1, n):    
   if string[i] not in word:  
            word[string[i]] = i
#get the non repeated letters and store them in new variable
for key in word:
    newword+= key  
#print the output
print(newword)  