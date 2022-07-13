print('主线程执行代码')

# 从 threading 库中导入Thread类
from threading import Thread
from time import sleep
def threadFunc(arg1, arg2):
    print('子线程 开始')
    print(f'线程函数参数是：{arg1}, {arg2}')
    sleep(5)
    print('子线程 结束')

thread = Thread(

    target=threadFunc,

    args=('参数1', '参数2')
)


thread.start()


thread.join()
print('主线程结束')
