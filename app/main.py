from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_input(input_str):
    return ''.join(char for char in input_str if char.isalnum() or char == '.' or char == '-')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_input(host)
    # Secure implementation with validation and escaping
    if not escaped_host:
        return {"status": "error", "message": "Invalid input"}
    subprocess.call(shlex.split(f'ping {escaped_host}'))
    return {"status": "completed"}