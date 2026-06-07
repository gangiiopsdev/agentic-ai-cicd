from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e.isdigit() or e in '-_.:/' and not e.isspace())
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Sanitize the input
    sanitized_host = sanitize_input(host)
    if not sanitized_host.strip():
        return {"status": "error", "message": "Invalid host provided"}
    try:
        # Safer implementation using list for subprocess arguments
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": e.stderr}