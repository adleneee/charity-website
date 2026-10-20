from flask import Flask, request
from markupsafe import escape

app = Flask(_name_)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        name = escape(request.form.get("name", ""))
        message = f"<h3>Thank you, {name}, for your support!</h3>"

    return f"""
    <html>
    <body style="text-align:center; font-family:Arial;
                 background:#eef7ff; padding:50px;">
        <h1>Hope Charity</h1>
        <h2>Together We Can Make a Difference</h2>
        <p>Help us support people in need.</p>

        <form method="POST">
            <input type="text" name="name"
                   placeholder="Enter your name" required>
            <button type="submit">Support Us</button>
        </form>

        {message}
    </body>
    </html>
    
        if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
    """