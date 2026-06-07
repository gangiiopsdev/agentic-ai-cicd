from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255 or any(char in host for char in [';', '&', '|', '$', '`']):
        return {"status": "error", "error": "Invalid input"}
    try:
        command = [os.path.join(os.sep, 'bin', 'ping'), host]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}