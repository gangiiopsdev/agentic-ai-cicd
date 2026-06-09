from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_command(command):
    return [part for part in shlex.split(command) if not part.startswith('/')]

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(safe_command('ping -c 4 ' + host), stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}