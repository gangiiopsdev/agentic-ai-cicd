from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    return shlex.quote(host)
app = FastAPI()
@app.get(
    "/",
    summary="Agentic Self-Healing Pipeline"
)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get(
    "/ping",
    summary="Ping a host",
    response_model={
        "status": str,
        "output": str
    }
)
def ping(host: str):
    try:
        sanitized_host = sanitize_host(host)
        output = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}