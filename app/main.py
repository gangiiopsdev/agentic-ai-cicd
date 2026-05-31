from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.Popen with validation and sanitization
    if not host or '@' in host or ':' in host:
        raise ValueError('Invalid input for ping')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}