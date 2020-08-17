class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i = 1
        while (i <= n):
            return [str(i) if(i%3!= 0 and i%5!= 0)  else(('Fizz'*(i%3==0)) + ('Buzz'*(i%5==0))) for i in range(1, n+1)]
        
        
    '''if the number is divisible by 3 then print "Fizz" , if the number is divisible by 5 then print "Buzz", if the number is divisible by both 3 and 5, then print "FizzBuzz" and if not
        then print the number itself.'''
        
        
        
        
        
        
        
        
        
        
        
        
