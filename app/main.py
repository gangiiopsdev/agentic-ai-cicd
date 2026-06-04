from fastapi import FastAPI
import subprocess
def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    result, _ = execute_command(command)
    return {"status": "completed", "result": result.decode()}