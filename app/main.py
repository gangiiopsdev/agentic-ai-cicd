from fastapi import FastAPI
import subprocess
def execute_safe_command(command, args):
    try:
        output = subprocess.run([command] + args, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = execute_safe_command('ping', [host])
    return {"status": "completed", "result": result}