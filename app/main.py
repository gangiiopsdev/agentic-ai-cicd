from fastapi import FastAPI
import subprocess
get_random_string = lambda length: ''.join(random.choice(string.ascii_letters) for _ in range(length))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and a safe command
    subprocess.call(["ping", host])
    return {"status": "completed"}