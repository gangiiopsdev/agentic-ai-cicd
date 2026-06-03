from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output.decode()}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum():
        return 'Invalid host'
    return execute_ping(host)