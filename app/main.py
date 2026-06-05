from fastapi import FastAPI
import subprocess
import shlex

def execute_ping(host: str):
    try:
        # Use shlex.split to safely handle the host input
        command = ['ping'] + shlex.split(host)
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=5, shell=False)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output.decode()}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum():
        return 'Invalid host'
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output.decode()}"