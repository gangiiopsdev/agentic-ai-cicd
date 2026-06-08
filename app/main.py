from fastapi import FastAPI
import subprocess
global process

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global process
    if process:
        process.terminate()
    # Validate the host input to ensure it does not contain harmful characters or patterns
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if any(char not in allowed_chars for char in host):
        return {"status": "error", "message": "Invalid host parameter"}
    # Use shlex.quote to safely escape the input
    import shlex
    process = subprocess.Popen(['ping', shlex.quote(host)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    return {"status": "completed", "output": process.communicate()}

@app.on_event("shutdown")
def stop_ping():
    global process
    if process:
        process.terminate()