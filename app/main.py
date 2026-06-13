from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(c in allowed_chars for c in host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):\n    if not is_safe_host(host): raise ValueError('Invalid hostname')\n\n    command = ['ping', host]\n    result = subprocess.run(command, capture_output=True, text=True, check=False, shell=False)\n\n    return {'status': 'completed', 'output': result.stdout}