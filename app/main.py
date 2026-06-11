from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    # Secure implementation
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = execute_ping(host)
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"error": str(e), "status": "failed"}