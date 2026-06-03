from fastapi import FastAPI
import subprocess
get_random_string = lambda length: ''.join(random.choice(string.ascii_lowercase) for i in range(length))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = subprocess.list2cmdline([host])
    try:
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        output = e.output
    return {"status": "completed", "output": output.decode()}