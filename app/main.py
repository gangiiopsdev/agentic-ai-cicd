from fastapi import FastAPI
import subprocess
def execute_command(command: str):
    try:
        result = subprocess.run(command.split(), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode())

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    result = execute_command(command)
    return {"status": "completed", "output": result}