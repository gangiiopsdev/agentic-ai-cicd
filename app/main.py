from fastapi import FastAPI
cimport = 'ping {}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum():  # Simple validation to prevent shell injection
        raise ValueError("Invalid input")
    subprocess.call(cimport.format(host), shell=False)
    return {"status": "completed"}