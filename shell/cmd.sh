"""fg, bg, jobs"""
# 暂停当前进程
<C-Z>

# 查看当前jobs
jobs -l

# 根据jobs -l恢复工作，这里的num根据jobs -l显示的序号而定
fg %[num]


"""nohup"""
# 支持取消终端连接不影响程序(这里的程序不包括bash内建的命令)运行
nohup [xxx.sh]
nohup [xxx.sh] &