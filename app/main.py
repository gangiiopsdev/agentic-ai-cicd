from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_safe_command(command, *args):
    try:
        result = subprocess.run([command] + list(args), check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.output}'

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    output = run_safe_command('ping', host)
    return {'status': 'completed', 'output': output}