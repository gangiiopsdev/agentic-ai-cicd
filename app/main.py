from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            # Validate host input (e.g., only allow alphanumeric and a few special characters)
            if not re.match(r'^[a-zA-Z0-9.-]{1,}$', host):
                raise ValueError("Invalid hostname")

            subprocess.call(["ping", host])
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    return SafePing.ping(host)