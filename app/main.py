from fastapi import FastAPI
import ping3

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        response_time = ping3.ping(host)
        if response_time is None:
            return {"status": "failed", "error": f'No response from {host}'}
        else:
            return {"status": "completed", "output": f'Response time: {response_time}s'}
    except Exception as e:
        return {"status": "failed", "error": str(e)}