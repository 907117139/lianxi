#身体质量指数BMI
def main():
    height = input("输入身高/m")
    weight = input("输入体重/kg")
    BMI = round(eval(weight)/pow(eval(height),2),1)
    if BMI <18.5:
        print(BMI, "国际BMI值：偏瘦")
        print(BMI, "国内BMI值：偏瘦")
    elif BMI>=18.5 and BMI <25:
        if BMI>=18.5 and BMI <24:
            print(BMI, "国际BMI值：正常")
            print(BMI, "国内BMI值：正常")
        else:
            print(BMI, "国际BMI值：正常")
            print(BMI, "国内BMI值：偏胖")
    elif BMI>=25 and BMI <30:
        if BMI>=25 and BMI <28:
            print(BMI, "国际BMI值：偏胖")
            print(BMI, "国内BMI值：偏胖")
        else:
            print(BMI, "国际BMI值：偏胖")
            print(BMI, "国内BMI值：肥胖")
    else:
        print(BMI, "国际BMI值：肥胖")
        print(BMI, "国内BMI值：肥胖")

for i in range(5):
    main()