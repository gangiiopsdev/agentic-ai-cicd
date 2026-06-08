from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['-', '.', '_'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to allow only valid characters
    if not all(c.isalnum() or c in ["-", ".", "_"] for c in host):
        return {"status": "error", "message": "Invalid host input"}
    sanitized_host = sanitize_input(host)
    command = ["ping", sanitized_host]
    result = subprocess.run(command, capture_output=True, text=True, check=False, shell=False)  # Added shell=False to prevent shell injection
    return {"status": "completed", "output": result.stdout}