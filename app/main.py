from fastapi import FastAPI
import subprocess
import shlex

global_safe_ping = lambda host: subprocess.run(['ping', shlex.quote(host)], check=True, capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    output = global_safe_ping(host)
    return {"status": "completed", "output": output.stdout}