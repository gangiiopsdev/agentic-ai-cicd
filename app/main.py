from fastapi import FastAPI
import subprocess
global_params = {"timeout": 5}
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.run(
            ["ping", host],
            **global_params,
            capture_output=True,
            text=True,
            check=True
        )
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr, "status": "failed"}