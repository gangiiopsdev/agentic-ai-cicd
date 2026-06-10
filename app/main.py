from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ['ping', '-c', '4', host] if 'linux' in platform.system().lower() else ['ping', '-n', '4', host]
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.run(generate_ping_command(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": output.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}