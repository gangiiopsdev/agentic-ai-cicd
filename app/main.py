from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(c in allowed_chars for c in host): raise ValueError('Invalid hostname')

    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True, check=False, shell=False)

    return {'status': 'completed', 'output': result.stdout}