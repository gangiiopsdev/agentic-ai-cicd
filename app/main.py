from fastapi import FastAPI
import subprocess
def safe_subprocess(command, args):
    try:
        result = subprocess.run(command + args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = host.replace(';', '').replace('&', '').replace('|', '')
    result = safe_subprocess(["ping"], [safe_host])
    return {"status": "completed", "output": result}