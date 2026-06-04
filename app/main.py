from fastapi import FastAPI
import subprocess
import re
def execute_ping(host: str):
    try:
        # Validate the host input to prevent command injection
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return 'Invalid host'
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output.decode()}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)