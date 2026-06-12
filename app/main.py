from fastapi import FastAPI
import subprocess
def escape_shell_argument(arg):
    return arg.replace("&", "\&").replace("|", "\|").replace(";", "\;")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(["ping", escape_shell_argument(host)])

    return {"status": "completed"}