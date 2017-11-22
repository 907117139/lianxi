def fact(n):
    if n ==0:
        return 1
    else:
        return n*fact(n-1)
n=eval(input("输入数字"))
print(fact(n),n)

def reverse(s):
    if s =="":
        return s
    else:
        return reverse(s[1:])+s[0]
s=input("输入要反转的字符串")
print(reverse(s))

