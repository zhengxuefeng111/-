from threading import Thread
#导入线程
from time import sleep
#导入睡眠时间
import time
#导入时间


# 调用时间模块
i = 500
job=0

times = time.time()
#全局变量
# 获取当前的时间
class chef(Thread):
    name = ''
    num = 0
    def run(self) -> None:
        global i, times
        while True:
            # 调用全局变量i
            times2 = time.time()
            # 调用当前时间
            if i < 500 and times2 - times < 60:
                # 判断柜子是否满，起止时间是否在规定时间内
                i += 1
                # 柜子的数量+1
                self.num = self.num + 1
            #     厨师做的蛋糕数
            elif times2 - times < 60:
                # 如果柜子满了且在时间内，暂停三秒
                sleep(3)
            else:
                print(self.name, '做了', self.num, '个蛋挞')
                print(self.num*1.5,'元工资')
                break
#                 超过时间直接打印每个人的蛋挞量，以及工资


p1 = chef()
p2 = chef()
p3 = chef()
# 赋值
p1.name = '青龙'
p2.name = '郑雪凤'
p3.name = '儿子'
# 命名
p1.start()
p2.start()
p3.start()
# 运行


class customer(Thread):
    # 定义类
    name = ''
    money = 5000
    # 属性

    def run(self) -> None:
        # 继承空值
        global i, times
        # 调用时间，柜子数量
        sal=0
        # 卖出的蛋挞个数
        while True:
            # 循环
            times2 = time.time()
            if self.money >= 3 and i > 0 and times2 - times < 60:
                self.money = self.money - 3
                i = i - 1
                # 柜子里的数量减一
                sal+=1
            #     柜子里数量减一，卖出就+1
            elif self.money >= 3 and i == 0 and times2 - times < 60:
                sleep(2)
            #     柜子数量等于零休眠

            else:
                print(self.name, '买了', i, '个蛋挞')
                print('总盈利',sal*3,'元')
                break
#                 没钱和超过时间直接打印每人打印的蛋糕以及盈利


c1 = customer()
c2 = customer()
c3 = customer()
c1.name = '11111'
c2.name = '22222'
c3.name = '33333'
c1.start()
c2.start()
c3.start()
