from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    return ''.join(ch for ch in host if ch.isalnum() or ch in ('.', '-'))

cmd = ['ping', shlex.quote(sanitize_host(host))]

app = FastAPI()

@app.get("")
    Returns a welcome message.")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get(
    "/ping",
    responses={
        200: {
            "description": "Returns the result of the ping command",
            "content": {"application/json": {"example": {"status": "completed", "output": "..."}}}
        }
    }
)
def ping(host: str):
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}