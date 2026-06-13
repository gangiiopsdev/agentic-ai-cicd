from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr.decode()}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    # Sanitize user input to prevent command injection
    sanitized_host = host.strip().replace(' ', '')
    if not sanitized_host:
        return {'status': 'error', 'message': 'Invalid input'}
    return ping(sanitized_host)