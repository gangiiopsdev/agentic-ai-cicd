from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Validate host input
        if not host.strip().isdigit():
            raise ValueError("Invalid host format")
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)