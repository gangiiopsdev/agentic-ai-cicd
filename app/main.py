from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Secure implementation
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        raise HTTPException(status_code=403, detail='Invalid host')
    return safe_ping(host)

allowed_hosts = ['127.0.0.1', '::1']