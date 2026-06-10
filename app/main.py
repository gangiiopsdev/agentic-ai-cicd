from fastapi import FastAPI
import subprocess
def execute_safe_command(command: str, *args):
    try:
        result = subprocess.run([command] + list(args), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if host.startswith('192.168.'):
        command = 'ping'
        args = [host]
        output = execute_safe_command(command, *args)
        return {"status": "completed", "output": output}
    else:
        return {"error": "Invalid host"}