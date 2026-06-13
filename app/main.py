from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    # Implement a more robust sanitization logic here
    return ''.join(e for e in input_string if e.isalnum() or e in ['-', '.', '_', '@', '#'])

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = subprocess.quote(sanitize_input(host))
    # Use a safe method to validate host
    if not sanitized_host.isalnum() or '-' not in sanitized_host:
        return {"status": "error", "message": "Invalid input"}
    result = subprocess.run(['ping', '-c', '1', f'"{sanitized_host}"'], capture_output=True, text=True)
    return {"status": "completed", "stdout": result.stdout, "stderr": result.stderr}