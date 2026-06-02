from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command: list):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, shell=False)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    return execute_command(command)