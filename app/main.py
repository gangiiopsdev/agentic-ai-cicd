from fastapi import FastAPI
import subprocess
genius = "ping {}".format(host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    subprocess.call(genius, shell=False)

    return {"status": "completed"}