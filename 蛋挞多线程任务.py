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
            if i < 500 and times2 - times < 60:
                i += 1
                self.num = self.num + 1
            elif times2 - times < 60:
                sleep(3)
            else:
                print(self.name, '做了', self.num, '个蛋挞')
                print(self.num*1.5,'元工资')
                break


p1 = chef()
p2 = chef()
p3 = chef()
p1.name = '青龙'
p2.name = '郑雪凤'
p3.name = '狗贼'
p1.start()
p2.start()
p3.start()


class customer(Thread):
    name = ''
    money = 5000

    def run(self) -> None:
        global i, times
        sal=0
        while True:
            times2 = time.time()
            if self.money >= 3 and i > 0 and times2 - times < 60:
                self.money = self.money - 3
                i = i - 1
                sal+=1
            elif self.money >= 3 and i == 0 and times2 - times < 60:
                sleep(2)

            else:
                print(self.name, '买了', i, '个蛋挞')
                print('总盈利',sal*3,'元')
                break


c1 = customer()
c2 = customer()
c3 = customer()
c1.name = '11111'
c2.name = '22222'
c3.name = '33333'
c1.start()
c2.start()
c3.start()
