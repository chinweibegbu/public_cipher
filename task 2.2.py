import random;
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode

""" 
If you want to use p and g as IETF suggestion respectively, uncomment them. 
The current implementation would be off of using the 37 and 5 respectively
"""

# p and g as hex values
p_hex = "B10B8F96 A080E01D DE92DE5E AE5D54EC 52C99FBC FB06A3C6 9A6A9DCA 52D23B61 6073E286 75A23D18 9838EF1E 2EE652C0 13ECB4AE A9061123 24975C3C D49B83BF ACCBDD7D 90C4BD70 98488E9C 219A7372 4EFFD6FA E5644738 FAA31A4F F55BCCC0 A151AF5F 0DC8B4BD 45BF37DF 365C1A65 E68CFDA7 6D4DA708 DF1FB2BC 2E4A4371"
g_hex = "A4D1CBD5 C3FD3412 6765A442 EFB99905 F8104DD2 58AC507F D6406CFF 14266D31 266FEA1E 5C41564B 777E690F 5504F213 160217B4 B01B886A 5E91547F 9E2749F4 D7FBD7D3 B9A92EE1 909D0D22 63F80A76 A6A24C08 7A091F53 1DBF0A01 69B6A28A D662A4D1 8E73AFA3 2D779D59 18D08BC8 858F4DCE F97C2A24 855E6EEB 22B3B2E5" 

# Function to return the decimal values of a string of hex values
def hex_value(p):
    p_split = p.split(" ")
    # new_p = [];
    new_p = ""
    for i in p_split:
        temp = int(i, 16)
        new_p += str(temp)
    # new_p = new_p.join()
    return int(new_p)

# p and g as decimals from the hex calc
# p = hex_value(p_hex)
# g = hex_value(g_hex)

# p and g as 37 and 5
p = 37
g = 5
g_prime = g

""" 
MALLORY'S ATTACK attack when she makes g=p-1
"""
g = p - 1
print("ATTACK DETECTED.... MALLORY HAS ATTACKED AND MADE g = p-1\n")


print("Printing the value of p and g")
print("p is currently", p ,"\ng is p-1 which is", g)

# Function for generating a random prime numbers in the range x and y, lower and upper bound respectively
def primesInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(n)
            
    return prime_list


# Select a random number from the prime number list which is from 1 to 1000 for Alice and Bob || Consider making it such that the number picked by Alice cant be the same as Bob
randomAlice = random.choice(primesInRange(1,1000));
randomBob = random.choice(primesInRange(1,1000));
print ("Alice's generated random number is: ", randomAlice, "\nBob's random number is:", randomBob);


# Function that can be used to calculate g^a*mod(p) or B = g^b*mod(p)
def modCalculator(uno,exponent):
    return (uno**exponent)%p

# Alice and Bob's first modular calculation
AlicePrimaryCalc = modCalculator(g, randomAlice);
BobPrimaryCalc = modCalculator(g, randomBob);
print("Alice's A is ", AlicePrimaryCalc)
print("Bob's B is ", BobPrimaryCalc)
print("Alice and Bob have the same number for A and B which is p - 1 and that is what they are exchanging")


# Alice and Bob's second modular calculation
AliceSecondaryCalc = modCalculator(BobPrimaryCalc, randomAlice);
BobSecondaryCalc = modCalculator(AlicePrimaryCalc, randomBob);
print("Alice's S is ", AliceSecondaryCalc)
print("Bob's B S ", BobSecondaryCalc)
print("Alice and Bob have the same number for S as well which is p - 1 and that is what they are encrypting")


print("\n\nMallory is aware that Bob and Alice have the same A,B and S and she knows it is p-1. Thus she can SHA encrypt p-1 and get the same key as them. Thus when they exchange their messages, Mallory can decrypt it\n")
print("\n\nAttack when Mallory makes g = 1\n\n")




""" 
g = 1
"""
p = 37
g = 5
g_prime = g

""" 
MALLORY'S ATTACK
"""
g = 1
print("\n\nATTACK DETECTED.... MALLORY HAS ATTACKED AND made g = 1\n")


print("Printing the value of p and g")
print("p is currently", p ,"\nand g is", g)


# Select a random number from the prime number list which is from 1 to 1000 for Alice and Bob || Consider making it such that the number picked by Alice cant be the same as Bob
randomAlice = random.choice(primesInRange(1,1000));
randomBob = random.choice(primesInRange(1,1000));
print ("Alice's generated random number is: ", randomAlice, "\nBob's random number is:", randomBob);


# Function that can be used to calculate g^a*mod(p) or B = g^b*mod(p)
def modCalculator(uno,exponent):
    return (uno**exponent)%p

# Alice and Bob's first modular calculation
AlicePrimaryCalc = modCalculator(g, randomAlice);
BobPrimaryCalc = modCalculator(g, randomBob);
print("Alice's A is ", AlicePrimaryCalc)
print("Bob's B is ", BobPrimaryCalc)
print("Alice and Bob have the same number for A and B,which is 1, and that is what they are exchanging")


# Alice and Bob's second modular calculation
AliceSecondaryCalc = modCalculator(BobPrimaryCalc, randomAlice);
BobSecondaryCalc = modCalculator(AlicePrimaryCalc, randomBob);
print("Alice's S is ", AliceSecondaryCalc)
print("Bob's B S ", BobSecondaryCalc)
print("Alice and Bob have the same number for S as well which is 1 and that is what they are encrypting")


print("\n\nMallory is aware that Bob and Alice have the same A,B and S and she knows it is 1. Thus she can SHA encrypt 1 and get the same key as them. Thus when they exchange their messages, Mallory can decrypt it\n\n")




""" 
g = p
"""
p = 37
g = 5
g_prime = g

""" 
MALLORY'S ATTACK
"""
g = p
print("\n\nATTACK DETECTED.... MALLORY HAS ATTACKED AND made g = p\n")


print("Printing the value of p and g")
print("p is currently", p ,"\nand g is", g)


# Select a random number from the prime number list which is from 1 to 1000 for Alice and Bob || Consider making it such that the number picked by Alice cant be the same as Bob
randomAlice = random.choice(primesInRange(1,1000));
randomBob = random.choice(primesInRange(1,1000));
print ("Alice's generated random number is: ", randomAlice, "\nBob's random number is:", randomBob);


# Function that can be used to calculate g^a*mod(p) or B = g^b*mod(p)
def modCalculator(uno,exponent):
    return (uno**exponent)%p

# Alice and Bob's first modular calculation
AlicePrimaryCalc = modCalculator(g, randomAlice);
BobPrimaryCalc = modCalculator(g, randomBob);
print("Alice's A is ", AlicePrimaryCalc)
print("Bob's B is ", BobPrimaryCalc)
print("Alice and Bob have the same number for A and B which is 0 and that is what they are exchanging")


# Alice and Bob's second modular calculation
AliceSecondaryCalc = modCalculator(BobPrimaryCalc, randomAlice);
BobSecondaryCalc = modCalculator(AlicePrimaryCalc, randomBob);
print("Alice's S is ", AliceSecondaryCalc)
print("Bob's B S ", BobSecondaryCalc)
print("Alice and Bob have the same number for S as well which is 0 and that is what they are encrypting")


print("\n\nMallory is aware that Bob and Alice have the same A,B and S and she knows it is 0. Thus she can SHA encrypt 0 and get the same key as them. Thus when they exchange their messages, Mallory can decrypt it\n\n")








