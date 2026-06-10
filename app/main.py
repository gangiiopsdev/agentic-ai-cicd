from fastapi import FastAPI
cimport subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host to prevent command injection and ensure it's a valid hostname
    if not host.isalnum() and '-' not in host:
        raise ValueError('Invalid host name')
    safe_host = shlex.quote(host)
    try:
        subprocess.run(['ping', '-c', '1', safe_host], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}