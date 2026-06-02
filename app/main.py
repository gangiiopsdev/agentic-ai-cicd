from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        # Validate and sanitize the host input
        if not host or not isinstance(host, str) or '\' in host or '"' in host or '<' in host or '>' in host or '|' in host or '&' in host or ';' in host or '(' in host or ')' in host or '`' in host:
            raise ValueError("Invalid input")
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    output = safe_ping(host)

    return {"status": "completed", "output": output}