from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    return subprocess.call(['ping', shlex.quote(host)])

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    try:
        result = execute_ping(host)
        return {"status": "completed", "result": result}
    except ValueError as e:
        return {"error": str(e)}