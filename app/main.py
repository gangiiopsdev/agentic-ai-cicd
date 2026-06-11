from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ["ping", str(host)]
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    subprocess.run(generate_ping_command(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": stdout.decode()}