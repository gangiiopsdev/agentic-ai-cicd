from fastapi import FastAPI
cimport subprocess

app = FastAPI()

def ping(host: str):
    safe_hosts = ['localhost', '127.0.0.1']
    if host.strip() in safe_hosts:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return {'status': 'completed' if result.returncode == 0 else 'error', 'message': result.stdout if result.returncode == 0 else result.stderr}
    else:
        return {'status': 'error', 'message': 'Invalid host'}

@app.get('/ping')
def ping_endpoint(host: str):
    # Sanitize input to prevent command injection
    if any(char in host for char in [';', '&', '|', '`', '$', '*', '?', '<', '>', '\']):
        return {'status': 'error', 'message': 'Invalid host'}
    return ping(host)