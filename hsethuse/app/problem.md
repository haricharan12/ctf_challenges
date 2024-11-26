# Math

- Namespace: picoctf/18739f24
- ID: Revise_Math
- Type: custom
- Category: Crypto
- Points: 50
- Templatable: yes
- MaxUsers: 1

## Description

This is a Flask-based web challenge centered around chemistry. The challenge is
designed to guide players through a series of hints embedded within the web 
pages, ultimately leading them to a "hidden search" endpoint. Players need to 
utilize various clues to find hidden paths and discover encrypted endpoints, 
unlocking further levels.


## Details

The application can be run by nc <IP> 5000


## Hints
1. The challenge involves multiple layers of encryption; pay attention to the 
sequence of decoding.
2. The key to deciphering lies in understanding historical cryptographic methods
 (hint: Giovan Battista Bellaso).
3. Carefully analyze the hint provided: K = 0.01720209895—it's not the key, 
but a clue to guide you.

## Solution Overview

1. Base64 Decoding: Start by decoding the given challenge string using Base64. 
This will provide the text that was encoded with ROT13.
2. Reverse ROT13: Apply ROT13 decryption to the Base64-decoded text. 
This will reveal the Vigenere cipher-encrypted string.
3. Decrypt Vigenere Cipher: Use the provided historical hint and knowledge of 
Giovan Battista Bellaso to realize that the Vigenere cipher is the encryption 
method. The key to decrypt is "CarlFriedrichGauss".

## Challenge Options

```yaml
cpus: 0.5
memory: 128m
pidslimit: 20
ulimits:
  - nofile=128:128
diskquota: 64m
init: true
```

## Learning Objective

- Investigate Layers of Encryption: Explore the given encoded challenge 
by systematically decoding each layer using Base64, ROT13, and the 
Vigenere cipher.
- Recognize Patterns and Hints: Identify subtle patterns in the hint 
(K = 0.01720209895) and the references to cryptographic history that point 
to the use of specific techniques or keys.
- Apply Cryptographic Techniques: Decode Base64, reverse ROT13, and decrypt 
using the Vigenere cipher with the provided key to uncover the original flag.

## Tags

- python

## Attributes

- author: Haricharan S
- organization: 18739
- event: 18739 CTF internal challenge