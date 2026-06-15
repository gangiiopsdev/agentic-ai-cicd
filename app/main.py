from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection
    if not host.isalnum():
        return {"status": "error", "output": "Invalid input"}
    args = ['ping', *shlex.split(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}