from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command):
    # Use subprocess.run safely without shell=True
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8')

@app.get("/ping")
def ping(host: str):
    try:
        command = ["ping", host]
        output = execute_command(command)
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"error": str(e)}