
Fibonacci = int(input('请输入斐波那契数列长度:'))
n = Fibonacci
fibs = [0,1]
for i in range(n):
    fibs.append(fibs[-1] + fibs[-2])
    #fibs.__len__(7)
print(fibs)