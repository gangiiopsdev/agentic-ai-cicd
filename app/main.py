from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> dict:
    try:
        # Validate and sanitize the host input more thoroughly
        safe_host = host.strip()[:100]
        if not re.match(r'^[a-zA-Z0-9.-]+$', safe_host):
            return {'status': 'error', 'message': 'Invalid host'}
        result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)