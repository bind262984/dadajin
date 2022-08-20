import time

result = 0
start = time.time()  # 返回运算前时间戳
for i in range(10000000):
    result +=  i
end = time.time() #返回运算后时间戳
print(result)
print(end  - start)