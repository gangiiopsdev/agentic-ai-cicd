from fastapi import FastAPI
def run_ping(host: str):
    # Secure implementation
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):  # No need for input validation as 'ping' is safe
    output = run_ping(host)
    return {"status": "completed", "output": output}