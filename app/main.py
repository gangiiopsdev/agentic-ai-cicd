from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Example of basic validation, adjust as needed
        return {'status': 'failed', 'error': 'Invalid input'}
    return run_ping(host)