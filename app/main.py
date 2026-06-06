from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host input to prevent injection attacks
        if not host.strip() or '<' in host or '>' in host or ';' in host or '&' in host or '|' in host or '$' in host:
            return {"status": "failed", "error": "Invalid input"}
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}