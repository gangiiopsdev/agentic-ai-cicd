from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(char for char in input_str if char in allowed_chars)

@app.get("/ping")
def ping(host: str):  
    sanitized_host = sanitize_input(host) 
    subprocess.call(['ping', sanitized_host], shell=False)  # Use a list instead of string to avoid shell=True
    return {'status': 'completed'}