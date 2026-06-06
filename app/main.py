from fastapi import FastAPI
import subprocess
generate_safe_command = lambda host: ['ping', '-c', '1', host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.run(generate_safe_command(host), check=True)
    return {"status": "completed"}