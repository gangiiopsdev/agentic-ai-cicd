from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input by validating or escaping the host parameter
    if not is_valid_host(host):
        return {'status': 'invalid input'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}

# Example validation function (adjust as needed)
def is_valid_host(host: str) -> bool:
    # Simple check to ensure the host contains only allowed characters
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return all(char in allowed_chars for char in host)