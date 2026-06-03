from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure alternative using subprocess.run with check=True and shell=False
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
home = ping