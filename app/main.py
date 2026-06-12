from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping_route(host: str):
    if validate_input(host):
        return ping(host)
    else:
        return {'error': 'Invalid input'}

def validate_input(input_str: str) -> bool:
    # Simple validation logic, can be more complex depending on requirements
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(char in allowed_chars for char in input_str)