from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        raise ValueError("Invalid input for ping")
    args = ['ping', shlex.quote(sanitized_host)]
    result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
    return {"status": "completed", "output": result.stdout}