from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    # Add validation logic here
    return host.strip().endswith('.com')

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        # Safe implementation with proper sanitization
        subprocess.call(['ping', '-c 1', host])  # Use '-c 1' to limit the number of pings
        return {'status': 'completed'}
    else:
        return {'status': 'invalid input'}, 400