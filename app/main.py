from fastapi import FastAPI
import subprocess
get_ip = subprocess.Popen(['ping', host], stdout=subprocess.PIPE)
output, error = get_ip.communicate()
if error:
    raise Exception(error.decode())