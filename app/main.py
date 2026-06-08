from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(c if c.isalnum() else '_' for c in host)

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    # Safe implementation
    result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'result': result.stdout}