from fastapi import FastAPI
import subprocess
def escape_input(user_input):
    return user_input.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    escaped_host = escape_input(host)
    try:
        result = subprocess.run(['ping', escaped_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}