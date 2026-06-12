from fastapi import FastAPI
import subprocess
def run_safe_ping(host):
    try:
        # Use shell=False and escape any special characters in host
        result = subprocess.run(['ping', subprocess.quote(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = run_safe_ping(host)
    return {"status": "completed", "output": output}