from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using parameterized command
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}