from fastapi import FastAPI
import subprocess
generate_random_string = lambda length: ''.join(random.choices(string.ascii_letters + string.digits, k=length))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    random_string = generate_random_string(10)
    # Secure implementation using subprocess with args instead of shell=True
    subprocess.call(["ping", host])

    return {"status": "completed"}