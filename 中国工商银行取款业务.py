i = 0
name = 0
dict = {1: ['中国工商银行', name, '123456', 1000000000, 'adres']}


def withdraw():  # 取款
    id = int(input('请输入账号：'))
    password = input('请输入密码：')
    withdraw1 = int(input('请您输入取钱金额:'))
    name1 = bank(id, password, withdraw1)
    if name1 == 1:
        print('用户不存在')
    elif name1 == 2:
        print('密码输入错误')
    elif name1 ==3:
        print('余额不足！！！！！！')
    else:
        print('               取款成功！')




def bank(id, password, withdraw1):
    if id in dict:
        if password != dict[id][2]:
            return 2
        else:
            if withdraw1 <= dict[id][3]:
                dict[id][3] = dict[id][3] - withdraw1
                print('            恭喜您取款成功！！！')
                print('            您的当前余额为：%0.2f元' % dict[id][3])
            elif withdraw1 > dict[id][3]:
                return 3
    else:
        return 1


withdraw()
