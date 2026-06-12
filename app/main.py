from fastapi import FastAPI
import subprocess
import shlex

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in input_str if c in allowed_chars)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run to safely handle user input and avoid shell=True
    host = sanitize_input(host)
    result = subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}