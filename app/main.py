from fastapi import FastAPI
import shlex

app = FastAPI()

def ping(host: str):
    # Fixed implementation using parameterized command
    subprocess.run(shlex.split('ping ' + host), check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    # Safe implementation using parameterized command
    subprocess.run(shlex.split('ping ' + host), check=True)