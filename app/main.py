from fastapi import FastAPI
import subprocess
def execute_safe_ping(host):
    try:
        args = ['ping', host]
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = execute_safe_ping(host)
    if 'Request Timeout' in result:
        return {"status": "completed", "result": "failure"}
    else:
        return {"status": "completed", "result": "success", "output": result}