from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    if host.startswith('192.168.1.') or host.startswith('10.0.0.'):  # Example IP validation
        subprocess.call(['ping', '-c', '1', host])
    else:
        return {'status': 'Invalid host'}

@app.get("/ping")
def ping_endpoint(host: str):
    result = ping(host)
    if isinstance(result, dict) and 'status' in result:
        return result
    else:
        return {'status': 'completed'}