from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    # Implement your validation logic here
    return host.isalnum()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = shlex.split(f"ping -c 1 {host}")
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'status': 'completed', 'output': output.decode('utf-8'), 'error': error.decode('utf-8')}