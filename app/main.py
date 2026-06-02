from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    cmd = ["ping", host]
    output = execute_command(cmd)
    return {"status": "completed", "output": output}