from fastapi import FastAPI
import subprocess
def execute_safe_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    output = execute_safe_command(command)
    return {"status": "completed", "output": output}