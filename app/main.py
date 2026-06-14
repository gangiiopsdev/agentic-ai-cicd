from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], check=True, shell=False)
    return {'status': 'completed'}