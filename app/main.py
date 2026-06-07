from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        args = ['ping', '-c', '1', host]  # Use a specific command and limit the number of pings
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.strip().replace('.', '', 3).isdigit():
        return {'status': 'failed', 'error': 'Invalid hostname'}
    return safe_ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}