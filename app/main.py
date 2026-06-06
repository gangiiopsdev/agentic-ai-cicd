from fastapi import FastAPI
import subprocess
import shlex
import re

global allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 	\/.:;,-_=+[]{}()<>?|&*^%$#@!~`')

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e in allowed_chars)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    sanitized_host = sanitize_input(host)
    subprocess.call(['ping', shlex.quote(sanitized_host)])
    return {"status": "completed"}