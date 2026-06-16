from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input):
    return ''.join(e for e in input if e.isalnum() or e in [".", "-"])

def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Safe implementation
    subprocess.run(['ping', sanitized_host], check=True)
    return {'status': 'completed'}