#用生成器生成菲波那切数列，方法定义：F(0)=1，F(1)=1, F(n)=F(n - 1)+F(n - 2)（n ≥ 2，n ∈ N*）

def fib(max):
    n,prev,curr=0,0,1
    while n < max:
        yield curr
        prev,curr=curr,curr+prev
        n=n+1
# f=fib(5)
# for i in range(5):
#     print(f.__next__())
#生成的结果是：1,1,2,3,5

def foo():
    print("first")
    count=yield
    print(count)
    yield
a=foo()
a.send(None)
a.send(5)
#返回结果是：first，5






