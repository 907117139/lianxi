def addInterest(balance,rate):
    for i in range(len(balance)):
        balance[i]=balance[i]*(1+rate)
def test():
    amount=[1000,105,3500,739]
    rate=0.05
    addInterest(amount,rate)
    print(amount)

test()