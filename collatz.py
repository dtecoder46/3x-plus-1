#Number input
num_start=int(input("What number do you want to start at?: "))
num_end=int(input("What number do you want to end at?: "))
print()

#Actual 3x+1 code
for i in range(num_start,num_end+1):
    print("Current number:",i)
    while i!=1:
        if i%2 == 0:
            i=i/2
            print(i)
        elif i%2 != 0:
            i=(3*i)+1
            print(i)
    print()
