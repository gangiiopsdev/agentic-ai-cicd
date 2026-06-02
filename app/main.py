from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.strip():
        return {"error": "Host parameter is required"}
    args = ['ping', host]
    try:
        subprocess.run(args, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Preventive controls
- Use a whitelist of allowed hosts instead of allowing any host input.
- Validate the input using regular expressions to ensure it conforms to expected formats.