from flask import Flask, request, Response, render_template
import requests

app = Flask(
    __name__,
    template_folder="templates"
)

SERVICE_MAP = {
    "app1": "http://127.0.0.1:5001",
    "app2": "http://127.0.0.1:5002",
}

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def proxy(path):
    service_name = path.split("/")[0]

    if service_name not in SERVICE_MAP:
        return "Service not found", 404

    target_base = SERVICE_MAP[service_name]
    target_path = path[len(service_name):]
    target_url = target_base + target_path

    headers = {
        k: v for k, v in request.headers if k.lower() != "host"
    }

    # ⭐ 关键：告诉后端它被挂在 /app1 /app2 下
    headers["X-Forwarded-Prefix"] = f"/{service_name}"

    resp = requests.request(
        method=request.method,
        url=target_url,
        headers=headers,
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False,
    )

    excluded = ["content-encoding", "content-length", "transfer-encoding", "connection"]
    response_headers = [
        (k, v) for k, v in resp.headers.items() if k.lower() not in excluded
    ]

    return Response(resp.content, resp.status_code, response_headers)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
