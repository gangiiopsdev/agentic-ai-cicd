from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', *shlex.split(host)]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

@app.get("/ping")
def ping(host: str):
    if not is_safe_input(host):
        raise ValueError('Invalid input')
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}

def is_safe_input(input_str: str) -> bool:
    # Define a set of allowed characters
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-")
    # Check if all characters in the input are in the allowed set
    return all(char in allowed_chars for char in input_str)