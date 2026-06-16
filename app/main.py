from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate the input to ensure it does not contain malicious characters
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', shlex.quote(host)]
    return ' '.join(args)

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = safe_ping(host)
        # Use subprocess.run instead of f-string simulation
        result = subprocess.run(sanitized_host, shell=False, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'result': result.stdout}
    except Exception as e:
        return {'error': str(e)}