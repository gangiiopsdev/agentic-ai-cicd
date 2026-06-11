from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize the host input to avoid command injection
    safe_host = ''.join(c for c in host if c.isalnum() or c in ['-', '.'])
    args = ['ping', '-c', '1', safe_host]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'success', 'output': result.stdout.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)