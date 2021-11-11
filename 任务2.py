# '''
# 有以下一个列表，求其中是5的倍数的和
# a = [1,5,21,30,15,9,30,24]
# '''
# a=[1,5,21,30,15,9,30,24]
# sum=0
# for i in range(0,8):
#
#     # print(a[i])
#     if a[i]%5==0:
#         sum=sum+a[i]
# print(sum)
'''
有下列列表，请编程实现列表的数据翻转（京东金融的测试开发笔试题）
List = [1,2,3,4,5,6,7,8,9]
实现效果：list = [9,8,7,6,5,4,3,2,1]
'''
# List = [1,2,3,4,5,6,7,8,9]
# print(List[::-1])
#
'''
请编程统计列表中的每个数字出现的次数(百度初级测试开发笔试题)
List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
'''
# sum=0
# List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
# for q in range(1, 11):
#     for i in range(0,len(List)):#len取列表的长度
#
#         if List[i]==q:
#
#             sum=sum+1
#     print(sum)
#     sum=0
'''
1)	将中国所有省会城市添加到上述列表中



2)	广东成为第二大发达城市，将广东排在上海前面



3)	[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]这是中国GDP排名前8的城市的GDP数值，请统计前8城市的GDP总和，平均GDP。


'''
city_names = ['北京', '上海', '广东']
#
# while True:
#     city=input('请输入城市名')#input请输入
#     if city == 'q' or city == 'Q':
#         break
#     else:
#         city_names.append(city)
#     print(city_names)
# city_names[1],city_names[2]=city_names[2],city_names[1]
# print(city_names)
# a ,b,c=1,0,-1
# print(a,b,c)
# a,b,c=c,b,a
# print(a,b,c)

# 1)	这是中国GDP排名前8的城市的GDP数值，请统计前8城市的GDP总和，平均GDP。
# sum=0
# GDP=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# for i in range(0,8):
#     sum=sum+GDP[i]
# print(sum,'元')
# # print(sum/8,'元')
# print(sum/len(GDP),'元')
# 有以下一个列表，求其中是5的倍数的和
# # a = [1,5,21,30,15,9,30,24]
# 有以下一个列表，求其中是5的倍数的和
# sum=0
# a = [1,5,21,30,15,9,30,24]
# a = [1,5,21,30,15,9,30,24]
# for i in range(0,len(a)):
#     if a[i]%5==0:
#         # print(a[i])
#         sum=sum+(a[i])
# print('总',sum)
# 有下列列表，请编程实现列表的数据翻转（京东金融的测试开发笔试题）
# 有下列列表，请编程实现列表的数据翻转（京东金融的测试开发笔试题）
# List = [1,2,3,4,5,6,7,8,9]
# 实现效果：list = [9,8,7,6,5,4,3,2,1]
# 实现效果：list = [9,8,7,6,5,4,3,2,1]
# list = [9,8,7,6,5,4,3,2,1]
# print(list[::-1])
# 请编程统计列表中的每个数字出现的次数(百度初级测试开发笔试题)
# List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
# for times in range(1,len(List)):
#
#     print(times,List.count(times))


'''def listNum(a):
    sep = list(set(a))
    print(sep)
    dict1 = dict.fromkeys(sep, 0)
    print(dict1)
    x = 0
    while x < len(sep):
        dict1[sep[x]] = a.count(sep[x])
        x = x + 1
    return dict1


a = [21, 21, 21, 56, 56, 56, 56, 56, 56, 10, 10, 10, 10, 3, 5]
print(listNum(a))'''


'''
有下列列表，请编程实现列表的数据翻转（京东金融的测试开发笔试题）
List = [1,2,3,4,5,6,7,8,9]
实现效果：list = [9,8,7,6,5,4,3,2,1]
'''
# List=[1,2,3,4,5,6,7,8,9]
# print(List[::-1])

'''
请编程统计列表中的每个数字出现的次数(百度初级测试开发笔试题)
List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
'''
List=[1,4,7,8,2,1,3,4,5,9,7,6,1,10]
list1=list(set(List))#去除重复值
dact_1={}
for times in list1:
    dact_1[times]=List.count(times)
print(dact_1)













