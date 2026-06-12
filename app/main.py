from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f"ping {host}"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = generate_ping_command(host)
    try:
        subprocess.run(command, shell=False, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}

    return {"status": "completed"}