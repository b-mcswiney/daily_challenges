'''
QUESTION FOR THE DAY
The Atbash cipher is an encryption method in which each letter of a word is replaced 
with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.

Create a function that takes a string and applies the Atbash cipher to it.
'''

def atbash(plaintxt: str) -> str:
    """
    Takes plaintext and returns ciphertext with atbash cipher
    """
    p = "abcdefghijklmnopqrstuvwxyz"
    c = "zyxwvutsrqponmlkjihgfedcba"
    ciphertxt = ""

    for i in plaintxt:
        # Check if character is english letter, if not retain it in ciphertext and skip rest of loop
        if i not in p:
            ciphertxt += i
            continue

        # Save uppercase
        if i.isupper():
            ciphertxt += c[p.index(i)].upper()
        else:
            ciphertxt += c[p.index(i)]

    return ciphertxt

print(atbash("hello world!"))
print(atbash("svool dliow!"))
