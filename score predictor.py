runs=int(input("enter run scored:"))
wickets=int(input("enter wickets taken:"))
catches=int(input("enter catches taken:"))
totalpoints=(runs*1+wickets*25+catches*10)
print(totalpoints)

if (totalpoints >=100):
    print("star player of the match")
elif (totalpoints >=50):
    print("good performer")
else:
    print("needs improvement")    
    
