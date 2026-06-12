from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate or sanitize the input
    if not all(c.isalnum() or c in ['-', '.'] for c in host):
        raise ValueError('Invalid hostname')
    return safe_ping(host)