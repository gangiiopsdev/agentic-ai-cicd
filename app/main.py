from fastapi import FastAPI
cimport socket

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host using socket, not subprocess
        socket.gethostbyname(host)
        # Ping command without shell=True for security
        result = subprocess.run(["ping", "-c", "1", host], capture_output=True, text=True)
        return {"status": "completed", "result": result.stdout}
    except socket.gaierror:
        return {"status": "failed", "message": "Invalid hostname"}