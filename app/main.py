from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate host input
        if not isinstance(host, str) or len(host.strip()) == 0:
            return {'status': 'error', 'message': 'Invalid host'}
        # Use subprocess.run for safe execution with shell=False
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)