from fastapi import FastAPI
import subprocess
def execute_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output, error = execute_ping(host)
    if error:
        return {"status": "error", "output": error}
    else:
        return {"status": "completed", "output": output}