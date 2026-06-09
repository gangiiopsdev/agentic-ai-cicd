from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        args = ['ping', '-c', '1'] + shlex.split(host)
        output = subprocess.run(args, stderr=subprocess.STDOUT, capture_output=True, text=True)
        if output.returncode != 0:
            return {"status": "failed", "error": output.stderr}
        else:
            return {"status": "completed", "output": output.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}