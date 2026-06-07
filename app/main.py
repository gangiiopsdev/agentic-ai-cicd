from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    try:
        # Use shlex to safely parse the command line
        args = shlex.split(f"ping {host}")
        subprocess.run(args, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}