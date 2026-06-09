from fastapi import FastAPI
import subprocess
def run_command(command):
    try:
        output = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = ["ping", host]
    result = run_command(command)
    return {"status": "completed", "result": result}