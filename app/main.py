from fastapi import FastAPI
class SafePing:
    @staticmethod
def ping(host: str):
        if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
            raise ValueError("Invalid characters in host")
        safe_host = subprocess.list2cmdline([host])
        result = subprocess.call(['ping', '-c', '1', safe_host], shell=False)
        return {'status': 'completed'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return SafePing.ping(host)