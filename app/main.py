from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input')
    cmd = ['ping', shlex.quote(host)]
    return subprocess.run(cmd, stderr=subprocess.STDOUT, text=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}

# Additional checks and validation can be added here, such as whitelisting allowed hosts or using a more secure method for network communication.