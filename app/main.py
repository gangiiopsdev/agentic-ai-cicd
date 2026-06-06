from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    return ''.join(c if c.isalnum() else '_' for c in user_input)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', '-c', '1', sanitized_host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}