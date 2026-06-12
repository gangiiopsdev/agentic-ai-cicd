from fastapi import FastAPI
import subprocess
def execute_safe_command(command: str):
    # Split the command into a list of arguments safely
    args = command.split()
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return f'Command failed with error: {e}'
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Safe implementation
    try:
        result = execute_safe_command(f'ping -c 1 {host}')
        return {"status": "completed", "result": result}
    except Exception as e:
        return {"error": str(e)}