from fastapi import FastAPI
import subprocess

def safe_ping(host):
    try:
        args = ['ping', host]
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() and not all(c in '0123456789.-' for c in host):
        raise ValueError('Invalid hostname')
    sanitized_host = ''.join(char for char in host if char.isalnum() or char in '.-')
    return safe_ping(sanitized_host)