x=input("请输入分数")
score=eval(x)
if score>=60.0 and score <70.0:
    grade='D'
    print(score,grade)
elif score>=70.0 and score <80.0:
    grade = 'C'
    print(score, grade)
elif score>=80.0 and score <90.0:
    grade = 'B'
    print(score, grade)
elif score>=90.0:
    grade = 'A'
    print(score, grade)