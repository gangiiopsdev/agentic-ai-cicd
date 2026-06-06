from fastapi import FastAPI
import subprocess
class SanitizedString:
    def __init__(self, value):
        self.value = ''.join(char for char in value if char.isalnum() or char in '-:.')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = SanitizedString(host).value
    if not sanitized_host.strip():
        return {"status": "failed", "error": "Invalid input"}
    try:
        result = subprocess.run(['ping', f'-c 1 {sanitized_host}'], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}