from fastapi import FastAPI
import subprocess
def run_safe_command(command, args):
    try:
        result = subprocess.run([command] + args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = 'ping'
    args = [host]
    result = run_safe_command(command, args)
    return {"status": "completed", "result": result}