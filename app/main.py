from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return ''.join(filter(allowed_chars.__contains__, host))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.call(['ping', '-c', '1', sanitized_host])  # Limit the number of pings to mitigate impact
    return {'status': 'completed'}