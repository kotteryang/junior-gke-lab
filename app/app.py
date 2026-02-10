from flask import Flask
import os

app = Flask(__name__)

@app.get("/")
def home():
    app_version = os.getenv("APP_VERSION", "v1")
    message = os.getenv("APP_MESSAGE", "hello")
    feature = os.getenv("FEATURE_FLAG", "off")
    return f"Hello GKE Junior! version={app_version} message={message} feature={feature}\n"

@app.get("/healthz")
def healthz():
    return "ok\n"

@app.get("/readyz")
def readyz():
    return "ready\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
