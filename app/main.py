from fastapi import FastAPI
import subprocess
class Sanitizer:
    @staticmethod
def sanitize_host(host: str) -> str:
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
        return ''.join(char for char in host if char in allowed_chars)

app = FastAPI()

def ping(host: str):
    sanitized_host = Sanitizer.sanitize_host(host)
    args = ['ping', sanitized_host]
    subprocess.call(args)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)