from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(char for char in host if char.isalnum() or char in ('-', '.', ':'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    try:
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}