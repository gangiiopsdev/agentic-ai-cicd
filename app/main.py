from fastapi import FastAPI
import subprocess
import shlex
def safe_getinput(command):
    if not validate_input(command):
        raise ValueError('Invalid input')
    return subprocess.run(shlex.split(command), capture_output=True, text=True).stdout

def validate_input(input_str):
    # Enhanced validation logic to ensure the input is safe
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return all(char in allowed_chars for char in input_str)

def validate_host(host: str) -> bool:
    # Add validation logic to ensure the host is safe
    allowed_hosts = ['example.com', 'localhost']
    return all(char.isalnum() or char in '-._' for char in host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not validate_host(host):
        raise ValueError('Invalid host')
    result = safe_getinput(f'ping -c 4 {host}')
    return {"status": "completed", "result": result}