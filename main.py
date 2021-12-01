from time import sleep

from HTMLTestRunner import HTMLTestRunner
import unittest

# 1.扫描所有用例
tests = unittest.defaultTestLoader.discover(r"C:\Users\lenovo\PycharmProjects\pythonProject\day14", pattern="Test*.py")

# 2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title="计算器测试报告",
    description="加法运算",
    verbosity=1,
    stream=open(file="计算器.html", mode="w+", encoding="utf-8")
)

runner.run(tests)
sleep(10)
import zmail
for i in range(10):
    mail_content = {
        'subject': '叮，有你的邮件！！！！',
        'content_text': '点开即可阅读文字哦！！！！！！！ ',
        'attachments': 'C:\\Users\lenovo\PycharmProjects\pythonProject\day14\计算器.html'
    }

    server = zmail.server('1678918259@qq.com', 'fdrpynhrwkxrdeci')
    server.send_mail('1186743549@qq.com',mail_content)
    sleep(1)




