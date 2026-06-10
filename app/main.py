from fastapi import FastAPI
import subprocess
def execute_safe_command(command, args):
    try:
        result = subprocess.run([command] + args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.decode('utf-8')}"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    result = execute_safe_command(*command)
    return {'status': 'completed', 'result': result}