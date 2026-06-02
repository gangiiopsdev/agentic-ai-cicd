from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the host parameter
        sanitized_host = ''.join(filter(str.isalnum, host))
        output = subprocess.check_output(['ping', f'-c 4 {sanitized_host}'], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e.output)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}