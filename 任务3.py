'''
姓名  年龄  性别  编号   任职公司   薪资   部门编号


'''
# names = [
#     ["曹操","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["许褚", "45", "男", "230", "Tencent", 700 , "10"]]
# # i=0
# sum=0
# while i<=3:
#     print(names[i][-2])
# # print(i)
#     sum=sum+names[i][-2]
#     i += 1
# print('平均薪资是:',sum/4,'元')


'''i=0
sum=0
while i<=3:
    print(names[i][1])
# print(i)
    sum=sum+int(names[i][1])
    i += 1
print('平均年龄是:',sum/4,'岁')'''

'''
公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
'''
'''names.append(['刘备', '45', '男', '220', 'alibaba', 500, '30'])
print(names)
sel = 0
i = 0
while i <= 4:
    if names[i][2] == '男':
        sel += 1
    i += 1
print('男生有:', sel, '人')
print('女生有:', len(names) - sel, '人')'''

'''while True:
    i=0
    much=0
    clup=input('请输入部门编号：')#输入
    while i<=3:
        if clup in names[i]:
             much=much+1
        i+=1
    print(much)#部门'''
'''List = [
    ['罗恩', 23, 35, 44],
    ['哈利', 60, 77, 68, 88, 90],
    ['赫敏', 97, 99, 89, 91, 95, 90],
    ['马尔福', 100, 85, 90]]
i=0
while True:
    zongchengji = 0
    fen = input('请输入学生姓名：')
    if fen=='罗恩':


        zongchengji = sum(List[0][1:])
        print(zongchengji)
    elif fen=='哈利':
        zongchengji = sum(List[1][1:])
        print(zongchengji)
    elif fen=='赫敏':
        zongchengji = sum(List[2][1:])
        print(zongchengji)'''


# num=int(input('请输入一个数：'))
# while num !=0:
#     print(num%10)
#     num=num//10

def bubbleSort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


a = [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3]
bubbleSort(a)
print('排序后的数组')
for i in range(len(a)):
    print('%d' % a[i])#冒泡排序
