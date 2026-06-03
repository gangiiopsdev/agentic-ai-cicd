from fastapi import FastAPI
import ping3

app = FastAPI()

def ping(host: str):
    response_time = ping3.ping(host)
    if response_time is None:
        status = "failed"
    else:
        status = "completed"
    return {"status": status}

@app.get("/ping")
def ping_endpoint(host: str):
    result = ping(host)
    return result