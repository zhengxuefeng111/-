'''
dict = {"k1":"v1","k2":"v2","k3":"v3"}
'''
'''dict = {"k1":"v1","k2":"v2","k3":"v3"}
for i in dict:
    print(i)
for i  in dict:
    print(dict[i])
dict['k4']='v4'
print(dict)'''

#水果超市
info={
    '苹果':32.8,
    '香蕉':22,
    '葡萄':15.5
}
Friuts={
    '苹果':12.3,
    '草莓':4.5,
    '香蕉':5.8,
    '橘子':6.4,
    '樱桃':15.8
}
info = {
    '小明': {
        'fruits': {'苹果':4, '草莓':13, '香蕉':10},
        'money': 0
    },
    '小刚': {
        'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
        'money':0
    }
}
name=input('请输入小朋友的姓名')
if name in info:
    print(info[name]['fruits']['苹果']*Friuts['苹果'])








