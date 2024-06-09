number_of_students=100  # set the number of students as 100
locker_state=100*[False]  # use a list of 100 Boolean elements

for i in range(1,101):  
    change_locker_period=i  # the period between two lockers the students changes is equal to his index
    for m in range(i-1,100,i):  # student changes every multiple of his index lockers
        locker_state[m]=not locker_state[m]  # change the locker state

print("The numbers of open lockers are:")
for locker in range(0,100):
    if locker_state[locker] is True:  # if the locker is open
        print(locker+1,end=" ")  # print out the open lockers number
print("\n"+"The rest lockers are closed.")