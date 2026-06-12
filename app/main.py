from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(cmd):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    cmd = ["ping", host]
    result = execute_command(cmd)
    return {"status": "completed", "output": result}