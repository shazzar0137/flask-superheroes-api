from flask import request, jsonify
from app import app, db
from app.models import Hero, Power, HeroPower

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
