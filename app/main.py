from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure the host input is sanitized
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
    else:
        return 'Invalid host'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}