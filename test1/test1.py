from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# ⭐ 关键：信任 gateway 传来的前缀
app.wsgi_app = ProxyFix(app.wsgi_app, x_prefix=1)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(port=5001)
