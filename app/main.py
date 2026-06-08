from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Use shlex.quote to escape any special characters in the host input
    result = subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True, text=True)
    return {
        "status": "completed",
        "response": result.stdout
    }