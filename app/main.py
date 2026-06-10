from fastapi import FastAPI
cimport subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate the host input to prevent command injection
        if not is_valid_host(host):
            raise ValueError('Invalid host')
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

def is_valid_host(host: str) -> bool:
    # Implement host validation logic here
    return all(c.isalnum() or c in ('.', '-') for c in host)

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)