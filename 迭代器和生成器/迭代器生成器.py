#coding:utf-8
#引入sys模块
import sys
list = [1,2,3,4]

#it =iter(list)

#while True:
#    try:
#        print(next(it))
#    except StopIteration:
#        sys.exit()
#print("生成器")

def fibonacci(n):
    a,b,counter =0, 1, 0
    while True:
        if (counter >n):
            return
        yield a
        a, b = b, a+b
        counter += 1
f = fibonacci(10)


while True:
    try:
        print (next(f))
    except StopIteration:
        sys.exit()
