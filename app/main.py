from fastapi import FastAPI
import subprocess
cimport os
def run_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not os.path.isfile('/bin/ping'):
        raise Exception('Ping utility not found on the system.')

    result = run_ping(host)
    return {"status": "completed", "result": result}