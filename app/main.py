from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    safe_host = ''.join(char for char in host if char.isalnum() or char in ('.', '-', '_'))
    try:
        result = subprocess.run(['ping', safe_host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e}'

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'output': response}