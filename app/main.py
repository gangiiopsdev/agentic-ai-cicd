from fastapi import FastAPI
class SafePing:
    @staticmethod
def ping(host: str):
        # Sanitize the host parameter
        safe_host = host.strip()
        if not all(c.isalnum() or c in ['-', '.', '_'] for c in safe_host):
            raise ValueError("Invalid characters in host")
        subprocess.run(['ping', safe_host], check=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    SafePing.ping(host)