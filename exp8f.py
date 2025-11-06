"""Frontend Flask app: exp8f.py
- Serves a simple page that displays the generated plots from exp8_plots.
Run: python exp8f.py
"""
import os
from flask import Flask, send_from_directory, render_template_string

app = Flask(__name__)
PLOTS_DIR = os.path.join(os.path.dirname(__file__), "exp8_plots")

TEMPLATE = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Exp8 Plots</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 30px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; }
    .card { padding: 10px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
    img { width: 100%; height: auto; border-radius: 6px; }
    h2 { font-size: 18px; margin: 8px 0; }
  </style>
</head>
<body>
  <h1>Generated Plots (Exp8)</h1>
  <div class="grid">
  {% for p in plots %}
    <div class="card">
      <h2>{{ p }}</h2>
      <img src="/plots/{{ p }}" alt="{{ p }}">
      <p><a href="/plots/{{ p }}" download>Download</a></p>
    </div>
  {% endfor %}
  </div>
</body>
</html>
"""

@app.route("/plots/<path:filename>")
def serve_plot(filename):
    return send_from_directory(PLOTS_DIR, filename)

@app.route("/")
def index():
    if not os.path.isdir(PLOTS_DIR):
        return "<p>No plots found. Run the backend script to generate them.</p>"
    plots = [f for f in os.listdir(PLOTS_DIR) if f.lower().endswith(('.png','.jpg'))]
    return render_template_string(TEMPLATE, plots=plots)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
