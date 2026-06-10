from fastapi import FastAPI
import subprocess
def run_safe_command(command: list):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Command failed with error: {e.stderr}'

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = ['ping', host]
    output = run_safe_command(args)
    return {'status': 'completed', 'output': output}