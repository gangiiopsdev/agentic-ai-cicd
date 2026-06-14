from fastapi import FastAPI
import subprocess
def run_safe_command(command: str):
    try:
        result = subprocess.run(command, shell=False, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    safe_command = f'ping {host}'
    output = run_safe_command(safe_command)

    return {"status": "completed", "output": output}