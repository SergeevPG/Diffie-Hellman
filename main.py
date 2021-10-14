from collections import Counter
import re
Alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
key = 0


def caesar_encryption1(key, message, Alphabet, numProgram):
    key = int(key)
    encrypt_message = list(message)
    new_word = []
    new_alphabet = Alphabet.copy()
    # сдвиг массива
    new_alphabet = new_alphabet[-key:] + new_alphabet[:-key]

    if numProgram == 1:
        print(f'\n::: Caesar Encryption v1.0 :::\n\nOriginal Alphabet:\t{Alphabet}\nNew Alphabet:\t\t{new_alphabet}\nKey:\t\t{key}')
        print(f"\nMessage:\t\t\t\n\"{''.join(encrypt_message)}\"")
    for i in encrypt_message:
        if i in new_alphabet:
            new_word.append(new_alphabet[Alphabet.index(i)])
        else:
            new_word.append(i)
    new_word = "".join(new_word)
    if numProgram == 1:
        print(f'\nEncrypted message:\n\"{"".join(new_word)}\"\n\n::: Caesar Encryption v1.0 :::')
    return "".join(new_word)


class sender():
    def __init__(self, name):
        self.name = name
        self.other_key_partitial = None
        self.key_full = None
        self.key_partitial = None
        print(f"\n\t-----  {self.name}  -----")
        while True:
            print(f"Введите private key для {self.name}:")
            self.private_key = input()
            self.private_key = int(self.private_key)
            if self.private_key <= 0:
                continue

            print(f"Введите public key для {self.name}:")
            self.public_key = input()
            self.public_key = int(self.public_key)
            if self.private_key <= 0:
                continue
            break

    def create_partial_key(self):
        print(f"\n{self.name}\nKey partial = ({Alice.public_key} ^ {self.private_key}) mod {Bob.public_key}")
        self.key_partitial = (Alice.public_key ** self.private_key) % Bob.public_key
        print(f"{self.name} Key partial = {self.key_partitial}")

    def send_partial_key(self):
        if self.name == "Alice":
            self.other_key_partitial = Bob.key_partitial
            print(f"\nAlice ←-- {self.other_key_partitial} ←-- Bob")
        elif self.name == "Bob":
            self.other_key_partitial = Alice.key_partitial
            print(f"Alice --→ {self.other_key_partitial} --→ Bob")

    def create_full_key(self):
        print(f"\n{self.name}\nKey full = ({self.other_key_partitial} ^ {self.private_key}) mod {Bob.public_key}")
        self.key_full = (self.other_key_partitial ** self.private_key) % Bob.public_key
        print(f"{self.name} Key full = {self.key_full}")

    def send_message(self):
        print(f"\nКлюч (сдвиг): {self.key_full} mod {len(Alphabet)} = {self.key_full%len(Alphabet)}")

        # message = 'абвгдеёжзи'.lower()
        print(f"Введите фразу, которую хотите зашифровать: ")
        message = input().lower()

        message = caesar_encryption1(self.key_full % len(Alphabet), message, Alphabet, 1)
        print(message)

if __name__ == '__main__':
    # str1 = send_message()
    print("Alice ←-------→ Bob")
    print("\t\t  |")
    print("\t\t  ↓")
    print("       Hacker")
    Alice = sender('Alice')
    Bob = sender('Bob')
    print(f"\nАлгоритмически мы согласились использовать\n{Alice.name}\tpublic key - в качестве основы\n{Bob.name}\t\tpublic key - в качестве расчета mod")
    # Алгоритмически мы согласились использовать Bob pub key в качестве основы, а Alice pub key в качестве расчета %
    Alice.create_partial_key()
    Bob.create_partial_key()

    Alice.send_partial_key()
    Bob.send_partial_key()

    Alice.create_full_key()
    Bob.create_full_key()

    Alice.send_message()