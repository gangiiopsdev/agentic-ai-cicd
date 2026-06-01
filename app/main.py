from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping_safe(host: str):
    # Input validation for the 'host' parameter
    if not host or len(host) > 255:
        raise ValueError("Invalid host parameter")
    args = ['ping', host]
    subprocess.run(args)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=80)