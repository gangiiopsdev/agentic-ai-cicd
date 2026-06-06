from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host):
    try:
        command = shlex.split(f'ping {host}')
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    response = execute_ping(host)
    return {"status": "completed", "response": response}