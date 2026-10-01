"""Minimal Flask web UI for the calculator so it's visible in the preview."""

from flask import Flask, request, jsonify, render_template_string

from calculator import add, subtract, multiply, divide

app = Flask(__name__)

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Calculator</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: system-ui, -apple-system, sans-serif;
    background: #0f172a; color: #e2e8f0;
    display: flex; justify-content: center; align-items: center;
    min-height: 100vh;
  }
  .card {
    background: #1e293b; border-radius: 16px; padding: 2rem;
    width: 100%; max-width: 360px; box-shadow: 0 8px 32px rgba(0,0,0,.4);
  }
  h1 { font-size: 1.25rem; margin-bottom: 1.5rem; text-align: center; color: #38bdf8; }
  .display {
    background: #0f172a; border-radius: 8px; padding: 1rem;
    text-align: right; font-size: 2rem; margin-bottom: 1rem;
    min-height: 3.5rem; overflow: hidden; color: #f8fafc;
  }
  .grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: .5rem; }
  button {
    border: none; border-radius: 8px; padding: 1rem; font-size: 1.1rem;
    cursor: pointer; background: #334155; color: #e2e8f0; transition: background .15s;
  }
  button:hover { background: #475569; }
  button.op { background: #0ea5e9; color: #fff; }
  button.op:hover { background: #0284c7; }
  button.eq { background: #22c55e; color: #fff; }
  button.eq:hover { background: #16a34a; }
  button.clear { background: #ef4444; color: #fff; }
  button.clear:hover { background: #dc2626; }
  button.wide { grid-column: span 2; }
</style>
</head>
<body>
<div class="card">
  <h1>🧮 Calculator</h1>
  <div class="display" id="display">0</div>
  <div class="grid">
    <button class="clear" data-key="C">C</button>
    <button data-key="back">⌫</button>
    <button class="op" data-key="/">÷</button>
    <button data-key="7">7</button>
    <button data-key="8">8</button>
    <button data-key="9">9</button>
    <button class="op" data-key="*">×</button>
    <button data-key="4">4</button>
    <button data-key="5">5</button>
    <button data-key="6">6</button>
    <button class="op" data-key="-">−</button>
    <button data-key="1">1</button>
    <button data-key="2">2</button>
    <button data-key="3">3</button>
    <button class="op" data-key="+">+</button>
    <button class="wide" data-key="0">0</button>
    <button data-key=".">.</button>
    <button class="eq" data-key="=">=</button>
  </div>
</div>
<script>
const display = document.getElementById('display');
let current = '0', prev = null, op = null;
function render() { display.textContent = current; }
document.querySelectorAll('button').forEach(btn => {
  btn.addEventListener('click', () => {
    const k = btn.dataset.key;
    if (k === 'C') { current = '0'; prev = null; op = null; }
    else if (k === 'back') { current = current.length > 1 ? current.slice(0,-1) : '0'; }
    else if (k === '=') {
      if (prev !== null && op) {
        fetch('/api/calc', {method:'POST',headers:{'Content-Type':'application/json'},
          body: JSON.stringify({a: parseFloat(prev), b: parseFloat(current), op})})
          .then(r => r.json())
          .then(d => { if (d.error) { current = 'Error'; } else { current = String(d.result); } prev = null; op = null; render(); })
          .catch(() => { current = 'Error'; render(); });
        return;
      }
    } else if (['+','-','*','/'].includes(k)) {
      if (prev !== null && op) { /* chain - for simplicity just store */ }
      prev = current; op = k; current = '0';
    } else {
      if (current === '0' && k !== '.') current = k;
      else if (k === '.' && current.includes('.')) {}
      else current += k;
    }
    render();
  });
});
</script>
</body>
</html>"""


@app.route("/")
def index():
    return render_template_string(PAGE)


@app.route("/api/calc", methods=["POST"])
def calc():
    data = request.get_json()
    a, b, op = data.get("a"), data.get("b"), data.get("op")
    ops = {"+": add, "-": subtract, "*": multiply, "/": divide}
    if op not in ops:
        return jsonify({"error": "invalid operator"}), 400
    try:
        result = ops[op](a, b)
    except (TypeError, ZeroDivisionError) as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
