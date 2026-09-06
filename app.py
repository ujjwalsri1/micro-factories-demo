from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple demo data
order = {
    "created": False,
    "part": "",
    "quantity": 0,
    "material": "",
    "deadline": "",
    "factories": [],
    "total_produced": 0,
    "status": "Waiting for order"
}


@app.route("/", methods=["GET", "POST"])
def index():
    global order

    if request.method == "POST":
        part = request.form.get("part")
        quantity = int(request.form.get("quantity", 0))
        material = request.form.get("material")
        deadline = request.form.get("deadline")

        # Simple demo allocation
        factory_a = round(quantity * 0.30)
        factory_b = round(quantity * 0.40)
        factory_c = quantity - factory_a - factory_b

        order = {
            "created": True,
            "part": part,
            "quantity": quantity,
            "material": material,
            "deadline": deadline,
            "factories": [
                {
                    "name": "Factory A",
                    "location": "Pune, India",
                    "allocated": factory_a,
                    "produced": factory_a,
                    "status": "Complete"
                },
                {
                    "name": "Factory B",
                    "location": "Ahmedabad, India",
                    "allocated": factory_b,
                    "produced": int(factory_b * 0.60),
                    "status": "In Production"
                },
                {
                    "name": "Factory C",
                    "location": "Bengaluru, India",
                    "allocated": factory_c,
                    "produced": factory_c,
                    "status": "Complete"
                }
            ],
            "total_produced": (
                factory_a
                + int(factory_b * 0.60)
                + factory_c
            ),
            "status": "In Production"
        }

        return redirect(url_for("index"))

    return render_template("index.html", order=order)


if __name__ == "__main__":
    app.run(debug=True)
