from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"
)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize the input to prevent command injection
        if not host.replace('.', '').isdigit() or len(host.split('.')) != 4:
            raise ValueError("Invalid IP address format")
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}