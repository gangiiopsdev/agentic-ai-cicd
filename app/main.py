from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_input(input_str):
    # Add your sanitization logic here
    return input_str.strip()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    host = sanitize_input(host)
    subprocess.call(['ping', quote(host)])
    return {'status': 'completed'}