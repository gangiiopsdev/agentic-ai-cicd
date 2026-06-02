from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command: str):
    try:
        result = subprocess.run(command, check=True, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.stderr.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    result = execute_command(command)
    return {"status": "completed", "output": result}