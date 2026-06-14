from fastapi import FastAPI
import subprocess
def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

cmd_whitelist = ['ping']  # Define a whitelist of allowed commands

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in cmd_whitelist:
        command = ["ping", host]
        result = execute_command(command)
        return {"status": "completed", "result": result}
    else:
        return {"error": "Invalid command"}