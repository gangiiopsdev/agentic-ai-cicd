from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, host))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host == host:
        subprocess.call(['ping', '-c 1', f'{sanitized_host}'], shell=False)
    else:
        raise ValueError('Invalid characters in hostname')
    return {'status': 'completed'}