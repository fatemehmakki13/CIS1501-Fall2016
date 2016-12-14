def nfactorial(n):
     if n <= 0:
         return 0
     elif n == 1:
         return 1
     return n * nfactorial( n - 1 )
 
 def nfactorialFunctional(n):
     total = n
     while ( n > 1 ):
         n -= 1
         total *= n
 
 def _fib(n1, n2, nth, currentNth):
     if nth == currentNth:
         return n1  n2
     else:
         return _fib(n2, n1n2, nth, currentNth1)
 
 def fib(nth):
     if nth <= 0:
         return 0
     elif nth == 1:
         return 1
     elif nth == 2:
         return 1
     else:
         return _fib(1, 1, nth, 3)
 
 def fibFunctional(nth):
     if nth <= 0:
         return 0
     elif nth == 1:
         return 1
     elif nth == 2:
         return 1
     else:
         n1 = 1
         n2 = 1
         currentNth = 3
         while currentNth != nth:
             temp = n1
             n1 = n2
             n2 = temp
             currentNth=1
         return n1  n2
 
 
 print(fib(35))
 print(fibFunctional(35))
