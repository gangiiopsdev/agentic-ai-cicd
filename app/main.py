from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_command(command: str, args: list):
    try:
        output = subprocess.check_output([command] + args, stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return e.output

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    output = execute_safe_command("ping", [host])
    return {"status": "completed", "output": output}