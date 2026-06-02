from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize user input to prevent command injection
    safe_host = ''.join(c for c in host if c.isalnum() or c in ('.', ':', '-', '_'))
    subprocess.run(['ping', safe_host], check=True, text=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):