# My Own Stream Cipher (MOSC)
# Modified from Rivest Cipher 4
import ciphers.extendedVigenere as ev
import ciphers.playfair as pf
import ciphers.tools as tools
import base64

def get_key_schedule(key):
    # Uses the Key-scheduling algorithm (KSA)
    K = bytearray(key, encoding='utf-8')
    S = [i for i in range(0, 256)]
    j = 0
    for i in range(0, 256):
        j = (j + S[i] + K[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    return S


def generate_keystream(key, text_length):
    # Uses Pseudo-random generation algorithm (PRGA)
    keystream = list()
    S = get_key_schedule(key)
    i, j = 0, 0
    for idx in range(0, text_length + 257):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        u = S[t]
        if idx > 256:
            keystream.append(u)
    
    return keystream


def xor(keystream, stream):
    K = bytearray(keystream)
    if type(stream) is str:
        stream = bytearray(stream, encoding="utf-8")
    R = bytearray()
    for i in range(0, len(K)):
        R.append(K[i] ^ stream[i])  
    return R


def mosc_encrypt(plaintext, key):
    plaintext = tools.cleanse(plaintext)
    ciphertext_ev = ev.extendedVEncrypt(plaintext, key)
    ciph_ev_b64 = base64.b64encode(ciphertext_ev.encode('utf-8')).decode('utf-8')
    cipherstream_rc4 = xor(generate_keystream(key, len(ciph_ev_b64)), ciph_ev_b64)
    ciphertext = base64.b64encode(cipherstream_rc4).decode('utf-8')
    return ciphertext


def mosc_decrypt(ciphertext, key):
    cipherstream_rc4 = bytearray(base64.b64decode(ciphertext))
    ciph_ev_btarr = xor(generate_keystream(key, len(cipherstream_rc4)), cipherstream_rc4)
    ciphertext_ev = base64.b64encode(ciph_ev_btarr).decode('utf-8')
    plaintext = ev.extendedVDecrypt(ciphertext_ev, key)
    return plaintext
