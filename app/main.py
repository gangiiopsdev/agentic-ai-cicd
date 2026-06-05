from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isnumeric():
        raise ValueError('Invalid host')
    command = ['ping', '-c', '1'] + [host]
    return subprocess.run(command, capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = safe_ping(host)
    return {'status': 'completed', 'result': result.stdout}