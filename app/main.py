from fastapi import FastAPI
import subprocess
def run_safe_ping(host):
    args = ['ping', host]
    try:
        output = subprocess.check_output(args)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/" )
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return run_safe_ping(host)