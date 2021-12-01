from unittest import TestCase
# 调用unttest里的testcase系统
from Calc import Calc


# 调用计算机系统
class TestCalc(TestCase):
    # 子类调用父类
    def testAdd1(self):
        a = -6
        b = 5
        c = 11

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd2(self):
        a = -6
        b = 5
        c = -1

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd3(self):
        a = 5
        b = 0
        c = 5

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd4(self):
        a = 6
        b = 'b'
        c = '非法字符'

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd5(self):
        a = 5000000000000000000000000000000000000000000000000000000
        b = 6
        c = 5000000000000000000000000000000000000000000000000000006

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd7(self):
        a = -5
        b = '%'
        c = '非法字符'

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd8(self):
        a = '我'
        b = 'six'
        c = '输入非法'

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd9(self):
        a = ' '
        b = '5'
        c = '非法字符'

        calc = Calc()
        result = calc.minus(a, b)

        self.assertEqual(result, c)

    def testAdd10(self):
        a = 'six '
        b = 'five '
        c = '输入非法'

        calc = Calc()
        result = calc.add(a, b)

        self.assertEqual(result, c)

    def testAdd11(self):
        a = '我'
        b = 'six'
        c = '输入非法'

        calc = Calc()
        result = calc.minus(a, b)

        self.assertEqual(result, c)

    def testAdd12(self):
        a = '0'
        b = 7
        c = 7

        calc = Calc()
        result = calc.minus(a, b)

        self.assertEqual(result, c)

    def testAdd13(self):
        a = '1'
        b = ' '
        c = '输入非法字符'

        calc = Calc()
        result = calc.minus(a, b)

        self.assertEqual(result, c)

    def testAdd14(self):
        a = '我'
        b = 'six'
        c = '输入非法'

        calc = Calc()
        result = calc.minus(a, b)

        self.assertEqual(result, c)

    def testAdd15(self):
        a = ' '
        b = 5
        c = '输入非法字符'

        calc = Calc()
        result = calc.mulit(a, b)

        self.assertEqual(result, c)

    def testAdd16(self):
        a = 1
        b = 5
        c = 5
        calc = Calc()
        result = calc.mulit(a, b)

        self.assertEqual(result, c)

    def testAdd17(self):
        a = 'FIVE'
        b = 'six'
        c = '输入非法字符'

        calc = Calc()
        result = calc.mulit(a, b)

        self.assertEqual(result, c)

    def testAdd18(self):
        a = 1
        b = 5
        c = 0.2

        calc = Calc()
        result = calc.division(a, b)

        self.assertEqual(result, c)

    def testAdd19(self):
        a = 1
        b = ' '
        c = '输入非法字符'

        calc = Calc()
        result = calc.division(a, b)

        self.assertEqual(result, c)

    def testAdd120(self):
        a = 'six'
        b = 5
        c = '请输入阿拉伯数字'

        calc = Calc()
        result = calc.division(a, b)

        self.assertEqual(result, c)
