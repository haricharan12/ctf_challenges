# Chemistry-Themed Flask Web Challenge

## Overview

This is a Flask-based web challenge centered around chemistry. The challenge is
designed to guide players through a series of hints embedded within the web 
pages, ultimately leading them to a "hidden search" endpoint. Players need to 
utilize various clues to find hidden paths and discover encrypted endpoints, 
unlocking further levels.

## Prerequisites

1. **Docker**: Ensure Docker is installed on your system.
2. **Python 3**: The challenge is built with Python 3 and Flask, so knowledge 
of basic Python and Flask structure will be helpful.
3. **Cryptographic Knowledge**: Understanding basic AES-128 encryption 
(ECB mode) and Base64 encoding will be useful.
4. **Networking Tools**: Tools like `curl` or a browser with developer 
tools to interact with endpoints and inspect HTTP responses.

## Getting Started

1. **Clone the Repository**:
    ```bash
    git clone <your-repository-url>
    cd <project-directory>
    ```

2. **Build the Docker Image**:
    ```bash
    docker build . --build-arg FLAG=picoCTF{deadbeef} -t hsethuse
    ```

3. **Run the Docker Container**:
    ```bash
    docker run -p 5000:5000 --name hsethuse -it hsethuse
    ```

4. **Access the Challenge**:
   Open your web browser and navigate to `http://0.0.0.0:5000`. You’ll 
   be presented with a chemistry-themed interface.

## Challenge Walkthrough

### Main Objectives

- **Explore Tabs**: Each tab contains general chemistry content and subtle hints.
- **Discover Hidden Endpoints**: The "hidden search" endpoint is 
obfuscated, requiring players to uncover it based on hints.
- **Decrypt Encrypted Paths**: Some paths are encrypted with AES-128. 
Players will need to decrypt Base64 encoded paths to progress.
- **Solve for Flag**: The final endpoint contains a command execution 
feature where players can retrieve the flag by using specific commands.


## Hints

- Explore each tab for references to elements that are rare or hidden.
- The "hidden search" page has hints relating to rare or unstable elements 
in the halogen group.
- Use tools to decode Base64 and decrypt AES-128 encrypted endpoints.


## Docker Instructions

To stop the Docker container when finished, run:

```bash
docker ps
docker stop <container_id>