from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it does not contain harmful characters
    if any(char in host for char in "<>|&;`$*?~#^(){}[]\":
        return {"status": "error", "message": "Invalid input"}
    command = ["ping", *shlex.split(host)]
    result = subprocess.run(command, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}