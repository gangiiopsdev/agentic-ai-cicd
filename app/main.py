from fastapi import FastAPI
import subprocess
get_output = lambda cmd: subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = get_output(['ping', host])
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}