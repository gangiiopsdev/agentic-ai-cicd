from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def safe_ping(host):
    if not re.match('^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    command = ["ping", host]
    output = run_command(command)
    return {"status": "completed", "output": output}

@app.get(
    "/"
)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get(
    "/ping"
)
def ping(host: str):
    return safe_ping(host)