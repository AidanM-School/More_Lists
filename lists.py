def sum_of_odd_nums(n):
    odd_nums=[i for i in range(1,2*n,2)]
    return (sum(odd_nums))

def caesar_cipher(message, key):
    character_list=[ord(i)+key for i in (message)]
    character_list=bytes(character_list)
    return character_list.decode('ascii')

def fizzbuzz(n):
    fizzbuzz=[fizzerbuzzer(i) for i in range(1,n+1)]
    return fizzbuzz

def fizzerbuzzer(n):
    if n//15==n/15:
      return "fizzbuzz"
    elif n//5==n/5:
      return "buzz"
    elif n//3==n/3:
      return "fizz"
    return n

def main():
    print('Table of the sum for the first n odd numbers:')
    print('n\tsum')
    print('-'*16)
    for n in range(10):
        print('{}\t{}'.format(n, sum_of_odd_nums(n)))

    print()

    ciphertext = "Frpsxwhu#Vflhqfh#lv#qr#pruh#derxw#frpsxwhuv#wkdq#dvwurqrp|#lv#derxw#whohvfrshv1"
    print(caesar_cipher(ciphertext, -3))

    print()

    for i in fizzbuzz(25):
        print(i)

if __name__ == '__main__':
    main()