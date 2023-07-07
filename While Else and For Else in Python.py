#While Else and For Else in Python
"""
Syntax:
   while condition :
              while block statement
   else :
              else block statement
-------------------------------------
Syntax:
   for variable_name in sequence :
              for block statement
   else :
              else block statement

"""

# While Else & For Else

i=1
while i<=10:
    #if(i==8):
       # break;
    print(i)
    i+=1
else:
    print("Loop Completed")
print("-----------------------------------------")

for i in range(1,21):
    #if i==5:
        #break
    print(i)
else:
    print("For Loop Completed")
print("-----------------------------------------")