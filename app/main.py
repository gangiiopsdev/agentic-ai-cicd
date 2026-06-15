from fastapi import FastAPI
import subprocess

def run_ping(host: str):
    # Validate and sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host input')

    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/ping')
def ping(self, host: str):  # Note: 'self' is not needed for FastAPI methods
    return run_ping(host)