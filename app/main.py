from fastapi import FastAPI
import subprocess
import shlex
def escape_user_input(user_input):
    return shlex.quote(user_input)

app = FastAPI()

@app.get("/"
)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        cmd = ['ping', escape_user_input(host)]
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}