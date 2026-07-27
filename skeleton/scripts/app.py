"""
Sample Python Application
Created using Backstage Scaffolder
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        {
            "application": "${{ values.repoName }}",
            "system": "${{ values.system }}",
            "group": "${{ values.group }}",
            "component": "${{ values.component }}",
            "status": "Application is running successfully!"
        }
    )


@app.route("/health")
def health():
    return jsonify(
        {
            "status": "UP"
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)