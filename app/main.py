from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(c in allowed_chars for c in host): raise ValueError('Invalid hostname')

    # Use a whitelist of allowed hosts or use a safe command that does not require user input
    result = subprocess.run(['ping', 'example.com'], capture_output=True, text=True, check=False, shell=False)

    return {'status': 'completed', 'output': result.stdout}