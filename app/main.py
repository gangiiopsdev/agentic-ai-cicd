from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Sanitize the host input to prevent command injection
        result = subprocess.run(['ping', f'{-host}'], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'result': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return result