from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e == '.' or e == '-').strip()
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {sanitized_host}'), check=True, capture_output=True, text=True, timeout=5)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
    except Exception as e:
        return {"status": "error", "message": str(e)}