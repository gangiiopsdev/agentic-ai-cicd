from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and sanitization
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    if not all(char in allowed_chars for char in host):  
        raise ValueError('Invalid host name')
    subprocess.call(['ping', subprocess.list2cmdline([host])])
    return {'status': 'completed'}