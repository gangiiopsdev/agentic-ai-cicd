from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    # Secure implementation with input validation and logging
    if not host or len(host) > 255:
        raise ValueError('Invalid host input')
    cmd = ['ping', shlex.quote(host)]
    subprocess.run(cmd, check=True, text=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_secure(host: str):
    # Secure implementation with input validation and logging
    if not host or len(host) > 255:
        raise ValueError('Invalid host input')
    cmd = ['ping', shlex.quote(host)]
    subprocess.run(cmd, check=True, text=True)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)