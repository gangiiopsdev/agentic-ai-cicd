from fastapi import FastAPI
import shlex
def safe_ping(host: str):
    # Using shlex.split to safely split the command into arguments
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout.strip()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = safe_ping(shlex.quote(host))  # Sanitize user input using shlex.quote()
    return {"status": "completed", "output": response}