#Input a string from user on command line. String may have multiple commas e.g.
#"Welcome,to,Sunbeam,CDAC,Diploma,Course". Print each word individually. Hint: use strtok()
#function.

str = input("Enter a string")
x = str.split(",")
for i in x:
    print(i)