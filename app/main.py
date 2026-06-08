from fastapi import FastAPI
import subprocess
import shlex

async def safe_ping(host: str):
    # Safe implementation using list instead of string for shell=True
    args = ['ping', host]
    try:
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            return {'status': 'error', 'error': error.decode()}
        return {'status': 'completed', 'output': output.decode()}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    try:
        host = shlex.quote(host)
        result = await safe_ping(host)
        return result
    except Exception as e:
        return {'status': 'error', 'error': str(e)}