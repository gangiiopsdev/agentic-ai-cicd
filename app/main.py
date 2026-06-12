from fastapi import FastAPI
import subprocess
import shlex
global_config = {'ping_enabled': False}
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not global_config['ping_enabled']:
        return {"error": "Ping feature is disabled for security reasons."}, 403
    # Secure implementation using subprocess.Popen for safe command execution
    try:
        result = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = result.communicate()
        return {"status": "completed", "output": output.decode(), "error": error.decode()}
    except Exception as e:
        return {"error": str(e)}, 500