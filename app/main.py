from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    command = ["ping", host]
    output = execute_command(command)

    return {"status": "completed", "output": output}