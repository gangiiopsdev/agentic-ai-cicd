from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command: str):
    # Sanitize input to prevent command injection
    safe_command = [arg.strip() for arg in command.split(' ') if arg]
    try:
        result = subprocess.run(safe_command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Command failed with error code {e.returncode}: {e.stderr}"

def ping(host: str):
    # Use a safe function to avoid command injection
    from fastapi.responses import JSONResponse
    try:
        result = execute_command(f'ping {host}')
        return JSONResponse(content={"status": "completed", "output": result})
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent unexpected behavior
    if not host or ' ' in host:
        return JSONResponse(status_code=400, content={"error": "Invalid host parameter"})
    return {"status": "completed", "output": execute_command(f'ping {host}')}