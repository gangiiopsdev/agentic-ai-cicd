from fastapi import FastAPI
import subprocess
def run_command(command, args):
    try:
        output = subprocess.check_output([command] + args, stderr=subprocess.STDOUT, timeout=5)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return run_command('ping', [host])