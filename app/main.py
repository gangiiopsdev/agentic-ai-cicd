from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    ALLOWED_HOSTS = ['127.0.0.1', '192.168.0.1', '10.0.0.1']  # Add more as needed
    return host in ALLOWED_HOSTS
global_host = '127.0.0.1'  # Use a safe default or validate host input
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    full_command = f"ping {host}"  # Directly use the provided host without shell execution
    result = subprocess.run(full_command, capture_output=True, text=True, check=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}