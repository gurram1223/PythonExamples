class Test:
    a=10; #static var
    def __init__(self):  #constructor
        Test.b=20; #static var
        self.c=30
    def m1(self):  #instance method
        Test.d=40  #static var
        self.e=50;
    @classmethod
    def m2(cls):  #class method
        Test.f=60  #static var
        cls.g=70
    @staticmethod
    def m3():
        Test.h=80
t=Test()
t.m1()
Test.m2()
print(Test.__dict__)