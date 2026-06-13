from fastapi import FastAPI
import subprocess
def escape_host(host):
    return host.replace("\", "\\")

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_host(host)
    try:
        result = subprocess.run(['ping', escaped_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}