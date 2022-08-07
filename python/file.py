"""按行读取文件"""

# 方式一：推荐用在必须借助readlines()返回list的场景
for line in open('test.txt').readlines():
    print(line.rstrip())

# 方式二：推荐平时读取使用，性能好，简洁
for line in open('test.txt'):
    print(line.rstrip())
