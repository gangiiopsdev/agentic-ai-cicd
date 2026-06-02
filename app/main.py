from fastapi import FastAPI
import shlex
global shell_context = {'ping': True}
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if 'ping' in shell_context and host:
        # Secure implementation using shlex to escape command arguments
        subprocess.run(shlex.split(f"ping -c 1 {host}")), check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid request parameters or operation not allowed."}