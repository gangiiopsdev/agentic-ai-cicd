from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-:_'
    return ''.join(c for c in input_string if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Secure implementation using subprocess.run with shell=False and check=True
    result = subprocess.run(shlex.split(f"ping {sanitized_host}"), capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}