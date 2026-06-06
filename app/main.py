from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()
@app.get('/ping')
def ping(host: str):
    sanitized_host = ''.join(e for e in host if e.isalnum() or e in ['-', '.', '_', ' '])
    return safe_ping(sanitized_host)