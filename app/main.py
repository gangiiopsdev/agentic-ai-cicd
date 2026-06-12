from fastapi import FastAPI
import subprocess
def execute_safe_command(command, *args):
    try:
        result = subprocess.run([command] + list(args), capture_output=True, check=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using execute_safe_command
    return execute_safe_command("ping", host)