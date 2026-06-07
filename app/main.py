from fastapi import FastAPI
import subprocess
import shlex
def escape_input(input_str):
    return ''.join([c if c.isalnum() or c in '._-' else '_' for c in input_str])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        escaped_host = escape_input(host)
        args = shlex.split(f'ping {escaped_host}')
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}