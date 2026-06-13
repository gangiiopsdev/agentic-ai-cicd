from fastapi import FastAPI
import subprocess
generate_random_string = lambda length: ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    random_string = generate_random_string(10)
    subprocess.call(f"ping {random_string}", shell=True)
    return {"status": "completed"}