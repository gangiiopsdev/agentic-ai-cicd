from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    output = run_command(command)
    return {"status": "completed", "output": output}