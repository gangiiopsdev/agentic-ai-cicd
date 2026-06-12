from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate host input to prevent command injection
    if not all(c.isalnum() or c in '.-:/' for c in host):
        raise ValueError('Invalid host name')
    args = ['ping', host]
    return subprocess.run(args, capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'result': result.stdout}
    except ValueError as e:
        return {'error': str(e)}