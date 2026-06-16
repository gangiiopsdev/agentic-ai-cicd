from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in ('.', ':', '-', '_'))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_host(host)
    # Use subprocess.run instead of subprocess.call for better security and more features.
    result = subprocess.run(['ping', escaped_host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}