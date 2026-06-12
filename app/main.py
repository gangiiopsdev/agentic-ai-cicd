from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        return execute_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}
def validate_host(host: str) -> bool:
    # Implement validation logic here
    return True