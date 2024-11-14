# Reversing Python

- Namespace: w3bthr1ll3r/ctf
- ID: w3b_thr1ll3r
- Type: custom
- Category: Web Exploitation
- Points: 100
- Templatable: yes
- MaxUsers: 1

## Description

This is a Flask-based web challenge centered around chemistry. The challenge is
designed to guide players through a series of hints embedded within the web 
pages, ultimately leading them to a "hidden search" endpoint. Players need to 
utilize various clues to find hidden paths and discover encrypted endpoints, 
unlocking further levels.


## Hints

- Explore each tab for references to elements that are rare or hidden.
- The "hidden search" page has hints relating to rare or unstable elements 
in the halogen group.
- Use tools to decode Base64 and decrypt AES-128 encrypted endpoints.

## Solution Overview

1. **Find `/hidden_search`**: The hints across the pages point to "hidden" 
aspects, guiding you to enter "hidden_search" as the endpoint.
2. **Decrypt `quantum_leap`**: The `/hidden_search` endpoint provides encrypted 
clues. Decrypt using the AES key provided in the source code.
3. **Retrieve Flag**: At `/quantum_leap`, use the command allowed to `cat` the 
file with the flag.

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

- Investigate the web application for hidden clues and paths using HTML, 
JavaScript, and network analysis.
- Identify patterns and hints within the content that may suggest hidden 
features or restricted areas.
- Apply cryptographic techniques like Base64 decoding and AES decryption 
to reveal encoded information.

## Tags

- python

## Attributes

- author: Haricharan S
- organization: 18739
- event: 18739 CTF internal challenge