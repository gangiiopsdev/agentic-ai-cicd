from fastapi import FastAPI
import subprocess
get_ip = lambda host: subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = get_ip(host)
    return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode() if result.stderr else ''}