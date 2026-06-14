from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and args parameter
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}