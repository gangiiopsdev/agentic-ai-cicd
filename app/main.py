from fastapi import FastAPI
import subprocess
def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

global env_vars
env_vars = {'PATH': os.environ['PATH']}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    output = run_command(command)
    return {"status": "completed", "output": output}