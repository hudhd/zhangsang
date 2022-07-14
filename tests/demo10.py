shengao = int(input('输入你的身高：'))
tizhong = int(input('输入你的体重:'))
age = int(input('输入你的年龄:'))

if age < 10:
    print('10岁儿童不参与')
elif age < 60:
    bmi = tizhong / (shengao ** 2)
    if bmi > 24:
        print('体重过重了')
    elif bmi < 18:
        print('体重国庆')
    else:
        print('体重正常')
else:
    print('60岁以上不参加')
