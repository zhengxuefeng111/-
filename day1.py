'''
使用random模块，如何产生 50~150之间的数？
'''
import random
num = random.randint(50, 150)
print(num)


# ''''''
#
#
#
# print("****************************************")
# print("          12月份衣服销售数据")
# print("日期     服装名城   价格/件  库存数量  销售量/每日")
# print("1号      羽绒服     253.6   500      10      ")
# print("2号      牛仔裤     86.3    600      60      ")
# print("3号       风衣      96.8    335      43      ")


print('''日期	服装名称	价格/件	库存数量	销售量/每日
1号	羽绒服	253.6	500	10
2号	牛仔裤	86.3	600	60
3号	风衣	96.8	335	43
4号	皮草	135.9	855	63
5号	T血	65.8	632	63
6号	衬衫	49.3	562	120
7号	牛仔裤	86.3	600	72
8号	羽绒服	253.6	500	69
9号	牛仔裤	86.3	600	35
10号	羽绒服	253.6	500	140
11号	牛仔裤	86.3	600	90
12号	皮草	135.9	855	24
13号	T血	65.8	632	45
14号	风衣	96.8	335	25
15号	牛仔裤	86.3	600	60
16号	T血	65.8	632	129
17号	羽绒服	253.6	500	10
18号	风衣	96.8	335	43
19号	T血	65.8	632	63
20号	牛仔裤	86.3	600	60
21号	皮草	135.9	855	63
22号	风衣	96.8	335	60
23号	T血	65.8	632	58
24号	牛仔裤	86.3	600	140
25号	T血	65.8	632	48
26号	风衣	96.8	335	43
27号	皮草	135.9	855	57
28号	羽绒服	253.6	500	10
29号	T血	65.8	632	63
30号	风衣	96.8	335	78''')



'''
从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''
a = int(input('输入△的一个边'))
if a < 0:
    print('边长不能小于0')
b = int(input('输入△的一个边'))
if b < 0:
    print('边长不能小于0')

c = int(input('输入△的一个边'))
if c < 0:
    print('边长不能小于0')

if a + b > c and a + c > b and b + c > a:
    print('可以形成△')
    if a == b == c:
        print('你输入了一个等边△')
    elif a == b or a == c or b == c:
        print('你输入了一个等腰△')
    elif a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        print('你输入了一个直角△')
else:
    print('不可以构成△')

    '''
    编程实现下列图形的打印
    '''
    i = 6
    sum = 0
    while i >= 0:
        sum = sum + 1
        print(' ' * i, ' ❀' * (sum))
        i = i - 1



# num = 9
# while num > 0:
#     for i in range(1,num+1):
#         print(i, '*', num, '=', i * num, end='  ')
#
#     print('\t')
#         # for i in range(i,i+1):
#     num=num-1
k = 1
z=20
sum=0
for j  in range(1,21):
    for i in range(1,z+1):
        k=k*(i)
        # print(k,i)
    z=z-1
    sum=sum+k
    k = 1
print(sum)


'''
从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
'''
z = 1
sum = 0
max=0
while z < 11:
    zheng = int(input('请输入十个数'))
    if max<zheng:max=zheng

    print(zheng)
    z = z + 1
    # 求和公式
    sum = sum + zheng
    print('求和', sum)
print('平均',sum/10)
print(max)

A=56
B=78
实现效果：
A=78
B=56
'''
A=56
B=78
i=input('输入+,-')
if i=='+':
    print(56,78)
elif i=='-':
    C=A
    A=B
    B=C
    print(A,B)
else :
    print('输入非法')




'''
           # 实现输入10个数字，并打印10个数的求和结果
'''
z=1
sum=0
while z<11:
    zheng=int(input('请输入十个数字'))
    print(zheng)
    z=z+1
    #求和公式
    sum=sum+zheng
    # print('求和',sum)



'''
实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
'''
i=0
while i<3:#循环三次
    name,password=input('输入用户名') , input('请输入密码')#批量定义 input(输入）
    if name=='root'  and password=='admin':
        print('ok')
    else:#否则
        print('no')
    i=i+1#登录次数
    if i>=3:
        print('登录锁定!!!!!!!!!')
        break




