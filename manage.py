

class RSA_system:

    def __init__(self, primes):
        self.p, self.q = primes[0], primes[1]
        self.n = primes[0] * primes[1]
        self.phi = (self.p - 1) * (self.q - 1)

    def EEA(self, b):
        print("Running EEA")

        q_list = []

        o = self.phi
        m = b
        reduce = True
        while(reduce):
            holder = m
            m = o % m
            o = holder

            if((o % m) == 0):
                reduce = False

        print("GCD: " + str(m))

        if(m == 1):
            print("Valid b")
            self.b = b
            #GENERATE A

            return True
        else:
            print("Entered number not relatively prime to " + str(self.phi))
            return False
        

        


def createSystem():
    
    primes = getPrimes()

    cryptosystem = RSA_system(primes)

    getExponents(cryptosystem)
    
    #print(primes)
    #print(n)
    


def getExponents(s):

    b_str = input('Enter integer mod ' + str(s.n) + ' for an encryption exponent:\n')

    try:
        b = int(b_str)

        valid_b = s.EEA(b)

        if not valid_b:
            getExponents(s)
        
    except:
        print('Invalid value entered for b.')
        getExponents(s)
    


def getPrimes():
    primes = input('Enter values for prime numbers p,q:\n')

    primes = primes.split()

    p_list = []
    for i in primes:
        try:
            new_p = int(i)
            #ADD PRIMALITY TEST
            p_list.append(new_p)
        except:
            print('Non-numerical value entered.')

            p_list = getPrimes()

    return p_list



r = input('Select a mode: G - generate, E - encrypt, D - decrypt. \n')

if(r.upper() == "G"):
    print("Generating new RSA cryptosystem.")
    createSystem()