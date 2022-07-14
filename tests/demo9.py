var1 = [33, ['我的名字', '黑羽白月'], 'hello world!']

print(var1[-1])
print(var1[1][1])
var1[-1] = 'oh my god'
print(var1)
var1[1][1] = '摆月童子'
print(var1)

var2 = [33, ('我的名字', '黑羽白月'), 'hello world!']
var2[1] = ('我的名字', '拜月童子')
print(var2)
