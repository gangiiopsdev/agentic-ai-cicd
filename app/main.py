from fastapi import FastAPI
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], universal_newlines=True)
            return output
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    safe_pinger = SafePing()
    return safe_pinger.ping(host)