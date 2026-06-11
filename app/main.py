from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input):
    # Basic input sanitization (replace this with more robust validation)
    return ''.join(e for e in input if e.isalnum() or e in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):

    # Sanitize the host input to prevent injection attacks
    sanitized_host = sanitize_input(host)

    try:
        # Use subprocess.Popen instead of subprocess.call and avoid shell=True
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}