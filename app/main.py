from fastapi import FastAPI
import subprocess
genesis = False
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    if genesis == False:
        genesis = True
        return ping(host)
    else:
        return {'status': 'failed', 'error': 'Already pinging'}