# Math-Themed Crypto Challenge

## Overview

This challenge combines multiple layers of encryption to guide players through 
a series of decoding steps to retrieve the final flag. Players will need to 
use knowledge of cryptographic techniques, to uncover the dynamically generated 
flag. The challenge is designed to test problem-solving and cryptographic skills
 in a Dockerized environment

## Prerequisites

1. Docker: Ensure Docker is installed on your system.
2. Python 3: The challenge is built using Python 3. Understanding Python 
scripts and their structure will be helpful.
3. Cryptographic Knowledge: Knowledge of encoding/decoding techniques.
4. Text Decoding Tools: Tools or libraries (e.g., Python's base64 or online 
decoders) will assist in solving the challenge.

## Getting Started

1. **Clone the Repository**:
    ```bash
    git clone <your-repository-url>
    cd <project-directory>
    ```

2. **Build the Docker Image**:
    ```bash
    docker build . --build-arg FLAG=picoCTF{deadbeef} -t hsethuse
    OR 
    cmgr update
    ```

3. **Run the Docker Container**:
    ```bash
    docker run -p 5000:5000 --name hsethuse -it hsethuse
    OR 
    cmgr playtest <>
    ```

4. **Access the Challenge**:
   nc <IP> <5000>

## Challenge Walkthrough

### Main Objectives

##### Explore Encryption Layers:
- The challenge involves multiple encryption layers.
- Players will be presented with an encoded string and must decode it step by step.
##### Solve for the flag 
The final flag is hidden within the layers of encryption. 
Players must systematically decode each step to retrieve the original text.

## Hints

- Analyze the hints provided in the output for guidance on cryptographic 
techniques and the key.
= Make use of Python or online tools for decoding and decryption tasks


## Docker Instructions

To stop the Docker container when finished, run:

```bash
docker ps
docker stop <container_id>