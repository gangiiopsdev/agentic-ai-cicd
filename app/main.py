from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    # Use check_output instead of call and ensure proper error handling
    try:
        result = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.output).decode('utf-8')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}