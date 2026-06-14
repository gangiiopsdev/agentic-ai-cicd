from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host: str) -> str:
    # Basic sanitization example; real implementation may require more robust checks
    return ''.join(c for c in host if c.isalnum() or c in ('.', '-'))

@app.get="/"
async def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        args = shlex.split(f'ping {sanitized_host}')
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

    return {"status": "completed"}