from fastapi import FastAPI
class SafePing:
    @staticmethod
def safe_ping(host: str):
        args = ['ping', '-c', '1', host]
        try:
            subprocess.run(args, check=True)
        except subprocess.CalledProcessError as e:
            print(f'Ping failed with error {e}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafePing.safe_ping(host)
    return {"status": "completed"}