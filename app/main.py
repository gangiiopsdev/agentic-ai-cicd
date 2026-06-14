from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isnumeric() or int(host) < 1 or int(host) > 254:
        return {"error": "Invalid host range"}, 400
    args = ['ping', '{}'.format(subprocess.list2cmdline([host]))]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}