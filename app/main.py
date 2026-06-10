from fastapi import FastAPI
import subprocess
def shell_escape(s):
    return ''.join(c if c.isalnum() or c in '-_.' else '_' for c in s)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    host = shell_escape(host)
    subprocess.call(f'ping {host}', shell=False, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "stdout": stdout.decode(), "stderr": stderr.decode()}