from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
global_config = {
    'allowed_hosts': ['127.0.0.1', '::1'],
}
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in global_config['allowed_hosts']:
        raise ValueError("Invalid host format")
    return execute_ping(host)