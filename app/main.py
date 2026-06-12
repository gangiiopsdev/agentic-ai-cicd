from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Sanitize input to prevent command injection
        safe_host = host.replace(';', '').replace('&', '').replace('|', '')
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get('/ping')
def ping(host: str):
    return {'status': 'completed', 'result': safe_ping(host)}