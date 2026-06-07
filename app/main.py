from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr.strip()}'

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    output = execute_command(command)
    return {"status": "completed", "output": output}