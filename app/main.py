from fastapi import FastAPI
import subprocess
import shlex
global ping
app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use shlex to safely handle the host input
        args = ['ping'] + shlex.split(host)
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}