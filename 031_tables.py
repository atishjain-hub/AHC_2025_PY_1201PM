

tno=2

while tno<=10:
    print("Table for no = {}".format(tno))
    print("="*30)
    for c in range(1,13):
        print("{} * {} = {}".format(tno,c,(tno*c)))
    print("-"*30)
    tno=tno+1
print("Thank You!")

