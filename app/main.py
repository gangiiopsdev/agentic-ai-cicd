from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate host input
    if not validate_host(host):
        return {'error': 'Invalid host'}
    args = ['ping', host]
    subprocess.run(args)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return result
    else:
        return {'status': 'completed'}

def validate_host(host):  # Implement validation logic here
    return host.strip().replace('.', '').isdigit()