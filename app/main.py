from fastapi import FastAPI
import subprocess
def execute_command(command):
    result = subprocess.run(command, shell=False, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    output = execute_command(command)
    return {"status": "completed", "output": output}