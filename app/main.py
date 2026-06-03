from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_command(command):
    return [shlex.quote(arg) for arg in command]

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    safe_host = host.strip().replace(';', '').replace('&', '')  # Basic sanitization
    subprocess.run(safe_command(['ping', safe_host]), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}