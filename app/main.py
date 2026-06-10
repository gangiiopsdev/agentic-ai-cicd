from fastapi import FastAPI
import subprocess
def execute_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input
    if not host or 'ping' in host:
        command_parts = ["ping", subprocess.DEVNULL]
        output = execute_safe_command(command_parts)
        return {"status": "completed", "output": output}
    else:
        return {"error": "Invalid input"}