from fastapi import FastAPI
import subprocess
def escape_special_chars(s):
    return ''.join(c if c.isalnum() else '_' for c in s)

def validate_host(host: str):
    allowed_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    if not all(char in allowed_characters for char in host):
        raise ValueError("Invalid characters in host")

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    escaped_host = escape_special_chars(host)
    subprocess.call(['ping', '-c', '1', escaped_host])  # Use specific options to mitigate shell injection risk
    return {'status': 'completed'}