from fastapi import FastAPI
import subprocess
generate_random_payload = lambda: ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    subprocess.call(['ping', generate_random_payload()])
    return {"status": "completed"}