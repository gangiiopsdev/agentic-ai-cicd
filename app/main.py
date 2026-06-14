from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    # Validate and sanitize the host input
    if 'ping' in host or ';' in host:
        raise ValueError('Invalid input')

    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)