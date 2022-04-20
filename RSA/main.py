
from RSA import *


def to_int(val, default=0):
    try:
        return int(val)
    except (ValueError, TypeError):
        return default


def to_string(array):
    mess = ""

    for num in array:
        mess += chr(num)

    return mess


def to_num_array(msg):
    array = []

    for c in msg:
        array.append(ord(c))

    return array


def menu():
    run = True


    while run:
        zinute = str(input("Iveskite zodis kuri sifruosime: "))

        p = to_int(input("\nIveskite pirmini numeri p: "))
        while not Pirminis(p):
            print("\nIvestas skaicius nera pirminis!")
            p = to_int(input("\nIveskite nauja pirmini skaiciu: "))

        q = input("\nIveskite pirmini skaiciu q: ")
        q = to_int(q)
        while p == q:
            print("Skaiciai negali buti vienodi!")
            q = to_int(input("\nIveskite nauja pirmini skaiciu: "))
        while not Pirminis(q):
            print("\nIvestas skaicius nera pirminis!")
            q = to_int(input("\nIveskite nauja pirmini skaiciu: "))


        e, n = generate_public_key(p, q)
        enc = to_string(encrypt(e, n, zinute))
        print(f"Sifruota zinute {enc}")




        d, n = generate_private_key(e, n)
        dec = decrypt(d, n, to_num_array(enc))

        print(f"Desifruota zinute: {to_string(dec)}")



if __name__ == '__main__':
    menu()
