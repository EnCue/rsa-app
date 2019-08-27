import random as r
import math as m
import sqmultiply as sqm
#Prime generator algorithm based on Miller Rabin primality test

class Primes:

    def __init__(self):
        self.p = self.getPrime()

    def getPrime(self):

        primeFound = False
        primeRtrn = 0

        while not primeFound:
            n = r.randint(100, 1000)
            print(n)
            #n = 199

            allegedphi = n - 1
            d = allegedphi
            two_ex = 0

            while True:
                new_d = d/2
                if int(new_d) == new_d:
                    d = int(new_d)
                    two_ex += 1
                else:
                    break

            if(two_ex >= 1):

                confident = False
                iterations = 0

                while not confident:
                    a = r.randint(1, n)

                    isWitness = True
    
                    ad = sqm.exp_func(a, d, n)

                    for i in range(0, two_ex):
                        poTwo = 2**i

                        cand = sqm.exp_func(ad, poTwo, n)
    
                        if cand == 1 or cand == (n-1):
                            isWitness = False
                            break

                    if(isWitness):
                        print(str(n) + " is composite")
                        confident = True
                        
                    else:
                        print("Start new loop for different a value")
                        iterations += 1
                        if(iterations >= 5):
                            confident = True
                            primeFound = True
                            primeRtrn = n
            
        return primeRtrn
    
    



p = Primes()
print(str(p.p))



