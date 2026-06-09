from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        # Use subprocess.Popen for safe execution
        process = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return process.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = execute_ping(host)
    return {"status": "completed", "result": result}