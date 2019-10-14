#Suppose you have a list of tuples as follows:
#[( ‘John’, (‘Physics’, 80)) , (‘ Daniel’, (‘Science’, 90)), (‘John’, (‘Science’, 95)), 
#(‘Mark’,(‘Maths’, 100)), (‘Daniel’, (’History’, 75)), (‘Mark’, (‘Social’, 95))]
#Create a dictionary with keys as names and values as list of (subjects, marks) in sorted order.
#{John : [(‘Physics’, 80), (‘Science’, 95)]Daniel : [ (’History’, 75), (‘Science’, 90)]Mark : [ (‘Maths’, 100), (‘Social’, 95)]}

#the tube mentioned in the assignment
tub= [( 'John', ('Physics', 80)) , ('Daniel', ('Science', 90)), ('John', ('Science', 95)),
      ('Mark',('Maths', 100)), ('Daniel', ('History', 75)), ('Mark', ('Social', 95))]
#convert the tuble into dictionary with reverse to avoid the replication in the names(keys)
dic=dict((y, x) for x, y in tub)
#print the dictionary
#print(dic)
#create a new dictionary
newdic = {} 
#allocate the keys and values in the new dictionary 
for key, value in dic.items(): 
    if value not in newdic: 
        #reverse the key and value since the keys and values are already flipped
        newdic[value] = [key] 
    else: 
        #add the new values to the old one for each key
        newdic[value].append(key) 
# printing result 
print(newdic)