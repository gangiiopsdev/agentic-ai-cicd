from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Use a list for the command instead of shell=True
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    if not host.isdigit():
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)