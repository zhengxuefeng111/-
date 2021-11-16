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
