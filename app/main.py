from fastapi import FastAPI
import subprocess
def generate_command(host: str) -> list[str]:
    return ['ping', host]
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run(generate_command(host), check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}