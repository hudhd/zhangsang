def likename(arg1, arg2):
    name = arg1[-2:]
    age = arg2[-2:]
    ret = name + ':' + age
    return ret

a1 = likename('他的名字:关于', 'tsde年龄:12')
print(a1)
