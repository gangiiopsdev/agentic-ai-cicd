from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        args = ['ping', host]
        output = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return output.stdout.decode()
    except Exception as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)