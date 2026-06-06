from fastapi import FastAPI
import subprocess
def execute_command(command):
    try:
        result = subprocess.run(command.split(), capture_output=True, check=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    output = execute_command(command)
    return {"status": "completed", "output": output}