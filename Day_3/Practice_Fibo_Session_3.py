# fibonacci series until specific length

# Length of series
n = 111
# Series starts with
fibo = [0, 1]

# f(n)=f(n−1)+f(n−2) and f(1)=1 , f(2)=1 ; fibo sequence formula
for i in range(2, n):
    fibo.append(fibo[i - 1] + fibo[i - 2])

# extract the sequence from list and print
print(*fibo)
