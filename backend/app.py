from flask import Flask, request, jsonify
from flask_cors import CORS
from .summarizer import extract_issues


def create_app() -> Flask:
    app = Flask(__name__)
    # Allow requests from local dev servers (Vite default 5173) and any origin by default
    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.get("/health")
    def health() -> tuple[dict, int]:
        return {"status": "ok"}, 200

    @app.post("/analyze")
    def analyze():
        try:
            data = request.get_json(silent=True) or {}
            text = data.get("text", "")
            group = data.get("group")
            category = data.get("category")

            issues = extract_issues(text=text or "", group=group, category=category)
            # Normalize to list of dicts with minimal shape
            normalized = []
            for idx, issue in enumerate(issues):
                if isinstance(issue, dict):
                    normalized.append(issue)
                else:
                    normalized.append({
                        "id": f"iss-{idx}",
                        "summary": str(issue).strip(),
                        "quote": None,
                        "group": group,
                        "category": category,
                    })

            return jsonify({"issues": normalized})
        except Exception as exc:
            # Avoid leaking internals
            return jsonify({"error": "Failed to analyze text.", "detail": str(exc)}), 500

    return app


app = create_app()

if __name__ == "__main__":
    # Debug server for local development
    app.run(host="0.0.0.0", port=5000, debug=True)
