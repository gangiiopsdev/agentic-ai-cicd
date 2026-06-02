from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate host input to ensure it does not contain malicious content
        if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
            return {"status": "failed", "error": "Invalid input"}
        result = subprocess.run(shlex.split('ping ' + host), check=True, stdout=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}