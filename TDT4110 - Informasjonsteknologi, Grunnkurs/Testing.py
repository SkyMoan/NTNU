

def addition(x, y):
    product = x + y
    print(product)
#addition(5, 6)


def downCounter(x):
    while x <= 10 and x >= 0:
        print(x)
        x-=1
#downCounter(10)

def upCounter(x):
    for x in range (1,11):
        print (x)
        x+=1
#upCounter(0)


#x = 6;
#print(str(x) + "katt")

#for i in range(0, 2):
    #for j in range(0, 2):
        #for k in range(0, 2):
            #print(i, j, k)

Name = input("Please enter your name:")

print("your name is " + Name)