from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized_host = ''.join(char for char in host if char in allowed_chars)
    return sanitized_host

def ping(host: str):
    sanitized_host = sanitize_host(host)
    command = ['ping', sanitized_host]
    subprocess.run(command, capture_output=True, text=True, shell=False)
    return {'status': 'completed'}