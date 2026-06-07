from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = host.replace(';', '').replace('&', '')
    return safe_ping(sanitized_host)