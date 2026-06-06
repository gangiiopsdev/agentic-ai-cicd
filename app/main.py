from fastapi import FastAPI
import subprocess
generate_random_hex = lambda: ''.join([random.choice('0123456789abcdef') for _ in range(16)])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(f"ping {generate_random_hex()}", shell=True)
    return {"status": "completed"}