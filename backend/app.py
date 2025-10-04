import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from summarizer import extract_issues


def create_app() -> Flask:
    app = Flask(__name__)
    # Allow cross-origin requests for local dev and simple deployments
    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.get("/health")
    def health():
        return jsonify({"ok": True})

    @app.post("/analyze")
    def analyze():
        data = request.get_json(silent=True) or {}
        text = data.get("text", "")
        group = data.get("group")  # e.g., "People with disabilities"
        category = data.get("category")  # e.g., "Accessibility" or list of categories

        if not isinstance(text, str) or len(text.strip()) == 0:
            return jsonify({"error": "'text' is required"}), 400

        issues = extract_issues(text=text, group=group, category=category)
        return jsonify({"issues": issues})

    return app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app = create_app()
    app.run(host="0.0.0.0", port=port, debug=True)
