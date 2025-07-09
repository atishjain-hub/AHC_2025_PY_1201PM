def  disp(**a): # Here **a is called Keyword Var Length Param and whose type is <class,dict>
    print(a,type(a))

#main program
disp(sno=10,sname="RS",cm=40,cpp=50,py=60) # Function call-1--with 5 Kwd Var length args
disp(eno=100,ename="Ravi",hb1="Hungry",hb2="Sleep",hb3="Good",hb4="Reading") # Function call-2 with 6 kwd  var length args
disp(a=10,b=20,c=30,d=40) # Function call-3 with 4 kwd  var length args
disp(tno=1000,tname="KV") # Function call-4 with 2 kwd  var length args
disp(bno="BID234") # Function call-5 with 1 kwd  var length args
disp()
