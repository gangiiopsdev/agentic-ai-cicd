from fastapi import FastAPI
import subprocess
generate_random_payload = 'ping' + ''.join(random.choices(string.ascii_letters + string.digits, k=10))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call([generate_random_payload, host], shell=False)
    return {"status": "completed"}