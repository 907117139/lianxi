#average.py
def main():
    sum=0
    count=0
    moredate="yes"
    while moredate[0]=="y":
        x=eval(input("enter a number>>"))
        sum=sum+x
        count +=1
        moredate=input("Do you have more number(yes or no)")
    print("\n The average of the numbers is",sum/count)

main()