from fastapi import FastAPI
import subprocess
def execute_command(command):
    try:
        output = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    result = execute_command(command)
    return {"status": "completed", "result": result}