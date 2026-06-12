from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Sanitize the host input to prevent command injection
        safe_host = ''.join(char for char in host if char.isalnum() or char in '.-')
        subprocess.run(['ping', '-c', '1', safe_host], check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)