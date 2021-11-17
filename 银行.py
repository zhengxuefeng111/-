import random
Money=0
dict={}
i=0

def add():
    ID = random.randint(10000000, 99999999)  # random随机生成的整数
    name=input('请输入用户名：')
    password=input('请输入登录密码：')
    adress=input('请输入用户地址：')
    while True:
        if len(password) ==6 and password.isdigit():

            print('恭喜你添加用户成功！！!')

            dict[ID]=['中国工商银行',name,password,0,adress]
            print(ID,dict)
            break
        else:
            print('密码错误')
            password = input('请输入登录密码：')


def save():
    while True:
        name=int(input('请输入账号：'))

        if name in dict:

            Money = int(input('请输入存钱金额：'))
            dict[name][3]=dict[name][3]+Money
            print('恭喜您业务办理成功！！！')
            print('       您的当前余额为：%0.2f元'%dict[name][3])
            break
        else:
            print('账号输入错误')

def withdraw():
    while True:
        global i
        name=int(input('请输入账号：'))
        password=input('请输入密码：')
        withdraw1 = int(input('请您输入取钱金额：'))
        if name in dict:
            while i<3:
                if password!=dict[name][2]:
                    print('密码不正确')
                    password=input('请重新输入密码：')
                    i+=1

                else:
                    if withdraw1<=dict[name][3]:
                        dict[name][3]=dict[name][3]-withdraw1
                        print('            恭喜您取款成功！！！')
                        print('            您的当前余额为：%0.2f元'%dict[name][3])
                        break
                    elif withdraw1 >dict[name][3]:
                        print('余额不足')
                        break
            print('大傻逼回家洗洗睡！！！！！！！！！！！')
        else:
            print('账号不存在')
            name= int(input('请输入账号：'))



















print('*********************中国工商银行**********************')
print('*1.开户')
print('*2.存钱')
print('*3.取钱')
print('*4.转账')
print('*5.查询')
print('*6.Bye！')
print('************************************************************')
while 1:
    num = input('请选择您需要的业务：')
    if num=='1':
        add()
    elif num=='2':
        save()
    elif num=='3':
        withdraw()




