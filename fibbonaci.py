## Example 1: Using looping technique
def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
print(fib(5))
 
## Example 2: Using recursion
def fibR(n):
 if n==1 or n==2:
  return 1
 return fibR(n-1)+fibR(n-2)
print(fibR(5))
 
## Example 3: Using generators
a,b = 0,1
def fibI():
 global a,b
 while True:
  a,b = b, a+b
  yield a
f=fibI()
next(f)#f.next()
next(f)#f.next()
next(f)#f.next()
next(f)#f.next()
print(next(f))#f.next())
 
## Example 4: Using memoization
def memoize(fn, arg):
 memo = {}
 if arg not in memo:
  memo[arg] = fn(arg)
  return memo[arg]
 
## fib() as written in example 1.
fibm = memoize(fib,5)
print(fibm)
 
## Example 5: Using memoization as decorator
class Memoize:
 def __init__(self, fn):
  self.fn = fn
  self.memo = {}
 def __call__(self, arg):
  if arg not in self.memo:
   self.memo[arg] = self.fn(arg)
   return self.memo[arg]

import time
@Memoize
def fibq(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a

startTime = time.time()
print(fibq(200000))
elapsedTime = time.time() - startTime
print(elapsedTime)


