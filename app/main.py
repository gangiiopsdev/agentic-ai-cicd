from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate the host input to ensure it's a valid hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'output': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed' if isinstance(output, dict) else 'completed', 'output': output}