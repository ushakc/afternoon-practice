#Generator Excercises

#Problem 1
#Create a generator, primes_gen that generates prime numbers starting from 2.
def is_prime(n):
    i = 2
    if n == 2:
        return True
    while i <= (n ** 2):
        if n % i == 0:
            return False
        i = i + 2
    return True

def primes_gen():
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n

gen = primes_gen()
for _ in range(10):
    print(next(gen), end=' ')









# Expected output
# 2 3 5 7 11 13 17 19 23 29
#----------------------------------------------------------------------------

#Problem 2
#Create a generator, unique_letters that generates unique letters from
#the input string. It should generate the letters in the same order as
#from the input string.

# Expected output
# h e l o
def unique_letters(str):
    new_string = " "
    for ch in str:
        if ch not in new_string:
            new_string += ch + ' '
    yield(new_string)


for letter in unique_letters('hellooolHHHllleee'):
    print(letter, end=' ')
