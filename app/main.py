from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Sanitize input to avoid command injection
        sanitized_host = host.replace(';', ' ').replace('&', ' ')  # Basic sanitization
        output = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)