from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate and sanitize input
    allowed_hosts = ['localhost', '127.0.0.1']
    if host.strip() in allowed_hosts:
        args = ['ping', host]
        try:
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"error": str(e)}
    else:
        return {"error": "Invalid host"}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)