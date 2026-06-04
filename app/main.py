from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Ensure the host is a valid hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'status': 'failed', 'error': 'Invalid input'}
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)