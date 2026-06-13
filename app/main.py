from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command: str):
    try:
        output = subprocess.run(command.split(), capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    command = f"ping {host}"
    result = execute_command(command)

    return {"status": "completed", "result": result}