from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _validate_host(host):
    # Simple check for allowed characters
    return all(c.isalnum() or c in '-.' for c in host)

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not _validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', shlex.quote(host)], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}