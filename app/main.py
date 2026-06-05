from fastapi import FastAPI
import subprocess
def escape_command(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ['.', '-', '_', ' ', ',', ':', '@', '#', '$', '%', '&', '*', '+', '/', '=', '?', '^', '`', '{', '|', '}', '~'])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = escape_command(host)
    try:
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    except Exception as e:
        return {"status": "failed", "error": str(e)}