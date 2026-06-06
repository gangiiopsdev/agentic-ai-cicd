from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not all(c.isalnum() or c in '.-' for c in host):  # Basic validation of input
        return "Invalid input"
    command = ['ping', '-c', '1', host]  # Use list to avoid shell=True
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        return {"status": "success", "output": result.stdout}
    else:
        return {"status": "failure", "error": result.stderr}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'status' in result:
        return result
    else:
        return {"message": result}