class Test:
    count=0
    def __init__(self, val):
        self.val=val

#    def show(self, val):
    def show(self):
        print(self)
        print(self.val)

    @classmethod
    def cls_method(cls):
        print('これはクラスメソッドです')
        

test=Test('こんにちは')
test.show()
print(test.count)
for i in range(5):
    test.count+=1
    print(test.count)

Test.cls_method()