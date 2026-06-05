from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it is safe for use in the ping command
    if not validate_host(host):
        raise HTTPException(status_code=400, detail="Invalid host input")
    args = ['ping', '-c', '1', re.sub(r'[^a-zA-Z0-9.-]', '', host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

# Function to validate the host input
def validate_host(host: str) -> bool:
    # Regex pattern for a basic validation of hostname or IP address
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None