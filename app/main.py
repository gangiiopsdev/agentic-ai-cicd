from fastapi import FastAPI
import subprocess
def safe_subprocess_run(command: list[str]):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error code {e.returncode}")
        raise

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = subprocess.list2cmdline([host])
    command = ['ping', safe_host]
    safe_subprocess_run(command)
    return {'status': 'completed'}