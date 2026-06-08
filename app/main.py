from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    output = run_command(command)
    if isinstance(output, str) and 'error' in output.lower():
        return {"status": "error", "error": output}
    else:
        return {"status": "completed", "output": output}