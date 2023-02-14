import ciphers.myOwnStreamCipher as mosc
import ciphers.tools as tools
import ciphers.extendedVigenere as ev
import ciphers.playfair as pf

plaintext = "Where no counsel is, the people fall... (Proverbs 11:14)"
key = "11073"

print("Debug 1.")
print(plaintext)
ciphertext = pf.playfairEncrypt(plaintext, key)
print(ciphertext)
plaintext = pf.playfairDecrypt(ciphertext, key)
print(plaintext)
print("\n")

# S = mosc.get_key_schedule(key)
# print(S)

# keystream = mosc.generate_keystream(key, len(tools.cleanse(plaintext)))
# print(keystream)

# ciphertext = mosc.xor(keystream, tools.cleanse(plaintext))
# print(ciphertext)
# plaintext = mosc.xor(keystream, ciphertext)
# print(plaintext)

cipherstream = mosc.mosc_encrypt(plaintext, key)
print(cipherstream)
plaintext = mosc.mosc_decrypt(cipherstream, key)
print(plaintext)
