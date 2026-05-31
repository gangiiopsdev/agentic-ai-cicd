from fastapi import FastAPI
import subprocess
import shlex

# Define a safe list of allowed hosts
ALLOWED_HOSTS = ['127.0.0.1', '192.168.0.1', '10.0.0.1']  # Add more as needed

global_host = '127.0.0.1'  # Use a safe default or validate host input

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in ALLOWED_HOSTS:
        raise ValueError('Invalid host')
    full_command = get_full_command(['ping', host])  # Use the provided host instead of global_host
    result = subprocess.run(full_command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}