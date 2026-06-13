from fastapi import FastAPI
import subprocess
def execute_safe_command(command, *args):
    return subprocess.run(command.format(*args), check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the input to prevent command injection
        safe_host = subprocess.quote(host)
        execute_safe_command(f'ping {safe_host}')
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}