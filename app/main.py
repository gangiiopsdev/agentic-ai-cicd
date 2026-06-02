from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Ensure host is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        subprocess.call(['ping', '-c', '4', host])  # Use specific options for the ping command
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)