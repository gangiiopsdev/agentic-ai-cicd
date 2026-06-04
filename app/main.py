from fastapi import FastAPI
import asyncio

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run
    try:
        result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        return {'status': 'completed' if result.returncode == 0 else 'failed', 'output': output.decode(), 'error': error.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)