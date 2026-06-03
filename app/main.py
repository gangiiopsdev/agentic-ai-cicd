from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Replace unsafe ping implementation with a safe alternative using subprocess.Popen
    args = ['ping', host]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode('utf-8'), error.decode('utf-8')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output, error = safe_ping(host)
    status = 'completed' if not error else 'failed'
    return {"status": status, "output": output, "error": error}