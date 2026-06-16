from fastapi import FastAPI
import shlex

app = FastAPI()

def run_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return {"status": "error", "message": "Invalid input for host"}
    safe_host = shlex.quote(host)
    command_parts = shlex.split(f"ping {safe_host}")
    result = run_command(command_parts)
    return {"status": "completed", "result": result}