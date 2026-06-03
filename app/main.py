from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Safe implementation using subprocess.run
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    result = run_ping(host)
    return {"status": "completed", "output": result}