import sys
import getopt
import unittest


opts, args = getopt.getopt(sys.argv[1:],"p:")
pattern = opts[0][1]
# discover = unittest.defaultTestLoader.discover("./",pattern='test_case_**.py')
discover = unittest.defaultTestLoader.discover("./test_case/",pattern=pattern)
#方式一：
runner = unittest.TextTestRunner()
runner.run(discover)
# #方式二：
# fp = open("testHtml.html","wb")
# runner =  HTMLTestRunner.HTMLTestRunner(stream=fp,title='api测试报告',description='测试情况')
# runner.run(discover)