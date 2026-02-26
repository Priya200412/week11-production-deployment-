from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from prometheus_flask_exporter import PrometheusMetrics
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    env = os.getenv("FLASK_ENV", "development")

    if env == "production":
        app.config.from_object("config.production.Config")
    elif env == "testing":
        app.config.from_object("config.testing.Config")
    else:
        app.config.from_object("config.development.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    metrics = PrometheusMetrics(app)

    @app.route("/")
    def home():
        return jsonify({"message": "Production Ready Flask App 🚀"})

    @app.route("/health")
    def health():
        return jsonify({"status": "healthy"}), 200

    return app