from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters
    if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
        return {"error": "Invalid host input"}
    try:
        subprocess.run(['ping', f'\"{host}\"'], check=True)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
    return {"status": "completed"}