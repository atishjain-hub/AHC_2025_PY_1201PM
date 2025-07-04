
dobj={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE",-1:"-ONE",-2:"-TWO",-3:"-THREE",4:"-FOUR",-5:"-FIVE",-6:"-SIX",-7:"-SEVEN",-8:"-EIGHT",-9:"-NINE"}

d=int(input("Enter a Digit(0-9):"))

#res = dobj.get(d) if(dobj.get(d))!=None else "a Positive Number" if d>0 else "a Negative Number"
#print("{} is {} ".format(d,res))


res=dobj.get(d)

if res==None:
    if d>0:
        print("+ve")
    else:
        print("-Ve")
else:
    print(res)



