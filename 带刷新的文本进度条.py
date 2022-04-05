import time
scale=30
print("------执行开始------")
for i in range(scale+1):
    a,b='**'*i,'..'*(scale-i)
    c=(i/scale)*100
    print("\r{:^6.2f}%[{}->{}]".format(c,a,b),end="")
    time.sleep(0.3)
print("\n------执行结束------")