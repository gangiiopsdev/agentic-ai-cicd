from fastapi import FastAPI
class SafePing:
    @staticmethod
def safe_ping(host):
        args = ['ping', '-c', '1', '--'] + [host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = SafePing.safe_ping(host)
    return {"status": "completed", "output": output}