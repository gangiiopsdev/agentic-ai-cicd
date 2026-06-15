from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True, None
    except subprocess.CalledProcessError as e:
        return False, str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    success, output = run_ping(host)
    if success:
        return {"status": "completed", "output": output.decode()}
    else:
        return {"status": "failed", "error": output}