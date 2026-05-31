from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ['ping', host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it does not contain shell metacharacters
    if any(char in host for char in ';&`$*?{}[]|\'):  # Example of basic validation
        return {"error": "Invalid input detected"}
    subprocess.call(generate_ping_command(host))
    return {"status": "completed"}