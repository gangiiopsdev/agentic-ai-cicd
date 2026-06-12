from fastapi import FastAPI
import subprocess

def safe_ping(host):
    try:
        args = ['ping', '-c', '4', host]  # Limit the number of pings for security
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() and not all(c in '0123456789.-' for c in host):
        raise ValueError('Invalid hostname')
    return safe_ping(host)