from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize the input to prevent command injection
        if not host.strip() or '<' in host or '>' in host or '&' in host or ';' in host or '&&' in host or '\|' in host:
            return {"status": "failed", "error": "Invalid input"}
        # Use shlex to safely quote the argument
        output = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}