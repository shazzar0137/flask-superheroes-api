from flask import request, jsonify
from app import app, db
from app.models import Hero, Power, HeroPower
from flask import make_response

@app.route('/')
def index():
    html_content = """
    <html>
    <head>
        <title>Superhero Powers API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                padding: 40px;
                color: #333;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background-color: #fff;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #2c3e50;
                text-align: center;
            }
            p {
                font-size: 16px;
                line-height: 1.6;
            }
            ul {
                margin-top: 20px;
            }
            li {
                margin-bottom: 10px;
            }
            code {
                background-color: #eee;
                padding: 2px 5px;
                border-radius: 4px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🦸‍♀️ Welcome to the Superhero Powers API 🦸‍♂️</h1>
            <p>This is a Flask-based RESTful API for tracking superheroes and their superpowers.</p>
            <p>Use the endpoints below to explore the API via Postman or a browser:</p>
            <ul>
                <li><code>GET /heroes</code> - List all heroes</li>
                <li><code>GET /heroes/&lt;id&gt;</code> - Get a specific hero and their powers</li>
                <li><code>GET /powers</code> - List all powers</li>
                <li><code>GET /powers/&lt;id&gt;</code> - Get a specific power</li>
                <li><code>PATCH /powers/&lt;id&gt;</code> - Update a power (use Postman)</li>
                <li><code>POST /hero_powers</code> - Create a hero power relationship (use Postman)</li>
            </ul>
            <p>Open Postman and import the provided collection to test these endpoints.</p>
        </div>
    </body>
    </html>
    """
    return make_response(html_content, 200)


@app.route("/heroes")
def get_heroes():
    return jsonify([hero.to_dict() for hero in Hero.query.all()]), 200

@app.route("/heroes/<int:id>")
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.to_dict()), 200
    return jsonify({"error": "Hero not found"}), 404

@app.route("/powers")
def get_powers():
    return jsonify([power.to_dict() for power in Power.query.all()]), 200

@app.route("/powers/<int:id>")
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.to_dict()), 200
    return jsonify({"error": "Power not found"}), 404

@app.route("/powers/<int:id>", methods=["PATCH"])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    try:
        data = request.json
        power.description = data.get("description")
        db.session.commit()
        return jsonify(power.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400

@app.route("/hero_powers", methods=["POST"])
def create_hero_power():
    try:
        data = request.json
        new_hp = HeroPower(
            strength=data.get("strength"),
            power_id=data.get("power_id"),
            hero_id=data.get("hero_id")
        )
        db.session.add(new_hp)
        db.session.commit()

        return jsonify({
            **new_hp.to_dict(),
            "hero": Hero.query.get(new_hp.hero_id).to_dict(),
            "power": Power.query.get(new_hp.power_id).to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400
