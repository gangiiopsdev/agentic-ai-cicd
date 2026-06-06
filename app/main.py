from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    # Basic input sanitization
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_string if char in allowed_chars)

@app.get("/ping")
def ping(host: str):

    sanitized_host = sanitize_input(host)
    # Safe implementation using subprocess.Popen without shell=True
    result = subprocess.Popen(['ping', sanitized_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = result.communicate()

    return {'status': 'completed', 'output': output.decode('utf-8'), 'error': error.decode('utf-8')}