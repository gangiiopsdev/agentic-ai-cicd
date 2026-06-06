from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate host to ensure it does not contain malicious input
        if not is_valid_host(host):
            raise ValueError("Invalid host")
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

def is_valid_host(host: str) -> bool:
    # Simple validation to prevent common malicious patterns
    return not any(char in host for char in [';', '&', '|', '<', '>', '`', '$', '\', '/', '*', '?', '~', '{', '}', '[', ']', '^'])