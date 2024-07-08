from extra_func import *
from gmpy2 import mpz, powmod
from sha256 import *


#Diffie Hellman parameters
#both parties agrees to the prime
p = mpz(2**255 - 19)

#secret keys of two banks
s1 = mpz(105642767739455403368919587017885160105020111219562573584605124436743979060111)
s2 = mpz(66545149154628053945162392164793569629940758053462215952793267335962231677843)

def hash(list):
    hashed_list = []
    for entry in list:
        value = generate_hash(entry)
        hashed_list.append(mpz(int.from_bytes(value, byteorder='big')))

    return hashed_list
def power_list(list, s):
    new_list = []
    for entry in list:
        new_list.append(powmod(entry, s, p))

    return new_list
if __name__ == '__main__':
    #Bank 1 database and Bank 2 database
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #n=2**8
    #r = mpz(249239224773769732904012854682678334197)
    #list1 = gen_uniform_database(n, r)
    list2 = ['e', '1', 'a', 'z']
    #list2 =  gen_uniform_database(2**5, r)

    #Hash of the databases
    hashed_list1 = hash(list1)
    hashed_list2 = hash(list2)
 
    # Bank2 uses encryption and sends the list to Bank 1
    encrypted_list2 = power_list(hashed_list2, s2)

    # Bank1 encrypts its database and the list from Bank 2
    encrypted_list1 = power_list(hashed_list1, s1)
    encrypted_list21 = power_list(encrypted_list2, s1)
    
    #Now Bank2 has encrypted_list1 and encrypted_list21
    result = [0 for i in range(len(list2))]
    
    encrypted_list12 = power_list(encrypted_list1, s2)
    for i in range(len(list2)):
        for j in range(len(list1)):
            if encrypted_list21[i] == encrypted_list12[j]:
                result[i] = 1
    print(f"Result : {result}")


