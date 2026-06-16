from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}

def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

app.get("/")(home)
app.get("/ping")(ping)