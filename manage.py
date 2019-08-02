

class RSA_system:

    def __init__(self, primes):
        self.p, self.q = primes[0], primes[1]
        self.n = primes[0] * primes[1]
        self.phi = (self.p - 1) * (self.q - 1)

    def display(self):
        print('New RSA scheme created\n')
        print('Primes: ' + str(self.p) + ', ' + str(self.q))
        print('Modulus: ' + str(self.n))
        print('Phi(n): ' + str(self.phi))
        print('Public exponent: ' + str(self.b) + '\nPrivate exponent: ' + str(self.a))

    def Encrypt(self, msg):
        unreduced_e = msg ** self.b
        e = unreduced_e % self.n

        return e

    def Decrypt(self, msg):
        unreduced_d = msg ** self.a
        d = unreduced_d % self.n

        return d
    
    def EEA(self, b):
        print("Running EEA")

        q_list = []

        o = self.phi
        m = b
        
        #r_vals = []
        t_i = 0
        t_ii = 1
        
        reduce = True
        while(reduce):
            #r_vals.append(m)
            q = int(o / m)
            t_new = t_i - t_ii*q
            t_i = t_ii
            t_ii = t_new
            
            holder = m
            m = o % m
            o = holder

            if((o % m) == 0):
                reduce = False

        #print("GCD: " + str(m))
        #print(t_ii)
        #print(r_vals)

        if(m == 1):
            print("Valid b")
            self.b = b
            #GENERATE A

            a = t_ii
            
            if(a < 0):
                a = a + self.phi
            
            #prod = a * b
            #print(prod % self.phi)

            self.a = a

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

    return cryptosystem



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


def useScheme(cs):
    mode = input('Encrypt or decrypt a new integer (E or D)\n')

    if(mode.upper() == "E"):
        plaintext = input('Enter plaintext integer to be encrypted: ')
        try:
            msg = int(plaintext)
            encryptedmsg = cs.Encrypt(msg)

            print('Encrypted form of message: ' + str(encryptedmsg))
        except:
            print('Invalid plaintext entered. Try again.')
            useScheme(cs)
    elif(mode.upper() == "D"):
        e_plaintext = input('Enter encrypted message to be decrypted: ')
        try:
            e_msg = int(e_plaintext)
            msg = cs.Decrypt(e_msg)

            print('Encrypted form of message: ' + str(msg))
        except:
            print('Invalid plaintext entered. Try again.')
            useScheme(cs)
    



r = input('Select a mode: G - generate, E - encrypt, D - decrypt. \n')

if(r.upper() == "G"):
    print("Generating new RSA cryptosystem.")
    cs = createSystem()

    cs.display()
    print("\n\n")

    useScheme(cs)


#cs = RSA_system([7, 13])
#cs.EEA(11)

