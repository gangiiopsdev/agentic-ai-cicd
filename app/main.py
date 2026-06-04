from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Using subprocess.run instead of subprocess.call to avoid shell=True and prevent command injection
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "stdout": result.stdout.decode('utf-8'), "stderr": result.stderr.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "stdout": e.output.decode('utf-8'), "stderr": e.stderr.decode('utf-8')}