var1 = [33, ['我的名字', '黑羽白月'], 'hello world!']
var1.insert(2, '你好')
print(var1)
var1 = [33, ['我的名字', '黑羽白月'], 'hello world!']
var1.insert(1, '你好')
print(var1)
str1 = '大家好，我的名字叫：黑羽白月'
print(str1[str1.find('：') + 0:])
str1 = '大家好，我的名字叫：黑羽白月'
#  这个表达式返回的就是一个列表，里面包含了冒号前后的两个子字符串。
print(str1.split('：')[-1])

