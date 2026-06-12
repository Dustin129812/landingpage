from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="1">
        <title>Reloj Flask</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: #0a0a0a;
                color: #00ff88;
                font-family: Arial, sans-serif;
            }

            .clock {
                font-size: 80px;
                font-weight: bold;
                padding: 30px 50px;
                border: 2px solid #00ff88;
                border-radius: 15px;
                box-shadow: 0 0 25px #00ff88;
            }
        </style>
    </head>
    <body>

        <div class="clock" id="clock">--:--:--</div>

        <script>
            function updateClock() {
                const now = new Date();
                const h = String(now.getHours()).padStart(2, '0');
                const m = String(now.getMinutes()).padStart(2, '0');
                const s = String(now.getSeconds()).padStart(2, '0');
                document.getElementById("clock").innerText = `${h}:${m}:${s}`;
            }

            setInterval(updateClock, 1000);
            updateClock();
        </script>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)