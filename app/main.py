from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using subprocess.Popen and shell=False
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, shell=False)
    return {'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        return safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {'error': 'Ping failed', 'stdout': e.stdout.decode(), 'stderr': e.stderr.decode()}