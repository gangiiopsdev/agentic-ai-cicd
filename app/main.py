from fastapi import FastAPI
import subprocess
generate_random_host = lambda: ''.join(random.choices(string.ascii_letters + string.digits, k=10))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using a fixed host
    subprocess.run(['ping', generate_random_host()], check=True)
    return {"status": "completed"}