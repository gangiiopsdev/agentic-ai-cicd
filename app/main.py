from fastapi import FastAPI
import subprocess
def run_command(command, args):
    try:
        result = subprocess.run([command] + args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if 'ping' in command:
        args = [host]
        return run_command('ping', args)
    else:
        return {"error": "Invalid command"}