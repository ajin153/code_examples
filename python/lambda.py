"""在循环中使用lambda需要注意显式提供参数"""
def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x) # 这里需要显式的提供i=i，否则后续调用acts[i](xx)时i值永远为4
    return acts
acts = makeActions()
