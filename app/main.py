from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    # Escape any special characters in the host input to prevent command injection
    return ''.join(c if c.isalnum() or c in ['-', '.', '_'] else '_' for c in host)

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    # Use subprocess.run instead of subprocess.call with shell=True
    result = subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}