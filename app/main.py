from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        # Use a whitelist for allowed hosts to mitigate injection risk
        allowed_hosts = ['8.8.8.8', '127.0.0.1']
        if host in allowed_hosts:
            result = subprocess.run(['ping', '-c 4', f'"{host}"'], check=True, capture_output=True, text=True)
            return {"status": "completed", "output": result.stdout}
        else:
            return {"status": "failed", "error": "Host not allowed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return execute_ping(host)