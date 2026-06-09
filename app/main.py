from fastapi import FastAPI
import subprocess
def execute_command(command, *args):
    try:
        result = subprocess.run([command] + list(args), capture_output=True, text=True, check=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = 'ping'
    args = [host]
    output = execute_command(command, *args)
    return {"status": "completed", "output": output}