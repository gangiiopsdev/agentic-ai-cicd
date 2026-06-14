from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Validate the host input to prevent injection attacks
        if not host.strip():
            raise ValueError('Invalid hostname')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)