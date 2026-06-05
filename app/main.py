from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize the input
        if not host or len(host) > 255 or ' ' in host or '.' not in host:
            raise ValueError("Invalid host")
        args = ['ping', host]
        result = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": result.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": e.output.decode()}
    except ValueError as e:
        return {"status": "error", "output": str(e)}