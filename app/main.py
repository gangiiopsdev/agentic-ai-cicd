from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if 'ping' in host:
        return "Invalid input"
    # Use safe method for ping without shell=True
    try:
        output = subprocess.check_output(['ping', '-c', '1', subprocess.check_output(['echo', host], text=True).strip()], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'output': str(e.output)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if 'status' in result and result['status'] == 'completed':
        return {'status': 'completed', 'output': result['output']}
    else:
        return {'status': 'failed', 'output': result['output']}