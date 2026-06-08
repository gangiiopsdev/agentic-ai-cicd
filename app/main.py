from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use shlex.quote to escape the input and avoid shell injection
        subprocess.run(shlex.split('ping ' + host), check=True)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

    return {"status": "completed"}