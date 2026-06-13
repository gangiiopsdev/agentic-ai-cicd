from fastapi import FastAPI
import subprocess

def execute_ping(host):
    try:
        # Use subprocess.run instead of subprocess.call
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    sanitized_host = ''.join(c for c in host if c.isalnum() or c.isdigit())
    return execute_ping(sanitized_host)