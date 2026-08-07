"""จุดเริ่มต้นสำหรับรันแอปในเครื่อง: python run.py"""
import os

from app import create_app

app = create_app()

if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    port = int(os.getenv("PORT", "5000"))
    app.run(debug=debug, port=port)
