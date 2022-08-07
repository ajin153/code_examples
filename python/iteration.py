"""迭代元素"""
L = [1, 2, 3, 4, 5, 6]
# 方式一：使用range，好处是省空间，不会生成额外的list
for i in range(0, len(L), 2):
    print(L[i])

# 方式二：使用slice，好处是简洁，易读
for i in L[::2]:
    print(i)


"""给dict的元素根据key值排序"""
D = {'a':1, 'b':2, 'c':3}
for k in sorted(D): print(k, D[k], end=' ')
