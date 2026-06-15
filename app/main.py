from fastapi import FastAPI
import subprocess
def execute_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Command failed: {e.stderr}'
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Validate or sanitize host input
    if not validate_host(host):
        return {"error": "Invalid host"}
    command_parts = ["ping", host]
    output = execute_safe_command(command_parts)
    return {"status": "completed", "output": output}
def validate_host(host: str) -> bool:
    # Simple example of validation
    return host.replace('.', '').isalnum() and len(host.split('.')) == 4