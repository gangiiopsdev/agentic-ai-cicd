from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Use shlex.quote to safely escape the host parameter
    safe_host = shlex.quote(host)
    try:
        result = subprocess.run(['ping', '-c', '1', safe_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    if 'error' in response['status']:
        return response
    else:
        return response