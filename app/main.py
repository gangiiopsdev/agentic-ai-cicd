from fastapi import FastAPI
import subprocess
global pinger
pinger = subprocess.Popen(['ping', '-c', '1'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    pinger.stdin.write(f"{host}\n")
    pinger.stdin.close()
    stdout, stderr = pinger.communicate()
    return {"status": "completed", "stdout": stdout.decode(), "stderr": stderr.decode()}