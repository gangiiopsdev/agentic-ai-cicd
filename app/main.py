from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_handler(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    return ping(host)
def is_valid_host(host: str):
    # Implement your validation logic here, e.g., checking for common attack vectors.
    return True