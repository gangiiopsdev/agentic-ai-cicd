from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

app = FastAPI()
@app.get("/ping")
def ping_host(host: str):
    # Sanitize input to prevent command injection
    safe_host = host.strip().replace(';', '').replace('&', '')
    return ping(safe_host)