from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in '._-')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.check_output(f"ping {sanitized_host}", shell=True, text=True, timeout=5)
        return {"status": "completed", "output": output}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}