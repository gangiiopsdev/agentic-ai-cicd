from fastapi import FastAPI
import subprocess
def execute_command(cmd):
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e.output)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    if host not in ['google.com', 'example.com']:
        raise ValueError('Invalid host')
    cmd = ["ping", host]
    result = execute_command(cmd)
    return {"status": "completed", "result": result}