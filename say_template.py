#coding=utf-8
"""
模板模式

模式特点：定义一个操作中的算法骨架，将一些步骤延迟到子类中

程序实例：考试时使用同一种考卷（父类），不同学生上交自己填写的试卷（子类方法的实现）

"""

class TestPaper:
    def TestQuestion1(self):
        print("Test1：A. B. C. D.")
        print("(%s)" % self.Answer1())

    def TestQuestion2(self):
        print("Test1：A. B. C. D.")
        print("(%s)" % self.Answer2())

    def Answer1(self):
        return ""
    def Answer2(self):
        return ""

class TestPaperA(TestPaper):
    def Answer1(self):
        return "B"
    def Answer2(self):
        return "C"

class TestPaperB(TestPaper):
    def Answer1(self):
        return "D"
    def Answer2(self):
        return "D"

if __name__ == "__main__":
    s1 = TestPaperA()
    s2 = TestPaperB()
    print("student 1")

    s1.TestQuestion1()
    s2.TestQuestion2()
    print("student 2")

    s2.TestQuestion1()
    s2.TestQuestion2()