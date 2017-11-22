def fact(n):
    if n ==0:
        return 1
    else:
        return n*fact(n-1)

def main():
    n=6
    print(fact(n),n)
main()

def reverse(s):
    if s =="":
        return s
    else:
        return reverse(s[1:])+s[0]
s="hello"
print(reverse(s))