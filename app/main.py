from fastapi import FastAPI
globally_allowed_hosts = {"example.com", "localhost"}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in globally_allowed_hosts:
        subprocess.run(["ping", "/bin/ping", host], check=True)
    else:
        raise ValueError("Host not allowed")
    return {"status": "completed"}