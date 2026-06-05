from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        args = shlex.split(f'ping {host}')
        output = subprocess.check_output(args, universal_newlines=True, timeout=5)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}
    except Exception as e:
        return {"status": "error", "error": str(e)}