from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(char for char in input_str if char.isalnum() or char in ('-', '.', '_', '+'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}