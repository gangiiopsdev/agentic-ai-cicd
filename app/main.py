from fastapi import FastAPI
import subprocess
generate_random_string = lambda x: ''.join(random.choices(string.ascii_letters + string.digits, k=x))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    random_host = generate_random_string(10)
    # Safer implementation
    subprocess.call(['ping', random_host])

    return {"status": "completed"}