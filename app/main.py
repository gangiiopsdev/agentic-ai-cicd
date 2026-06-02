from fastapi import FastAPI
import subprocess
generate_random_string = "ping-" + ''.join(random.choices(string.ascii_letters, k=8))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with random filename to avoid command injection
    subprocess.call(["ping", generate_random_string])
    return {"status": "completed"}