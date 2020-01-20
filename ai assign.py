a= "I am human being".split()
b= "I am good".split()
c= "Good graders study well".split()
d= "Humans love graders".split()
e= "Every human does not study well".split()

f= {"every","human","good"}
st1=(input("Enter your statement: ")).split() #string to list conversion 
st2=set(st1) #kist to set conversion
if f.issubset(st2) or st1[0]=="Every" and st1[1]=="human" and st1[3]=="good" or st1[0]=="Every" and st1[1]=="human" and st1[4]=="good":
    print("no")
else: print("yes")
input("press enter to exit:")
