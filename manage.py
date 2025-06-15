from flask_migrate import Migrate
from app import app, db
from app.models import Hero, Power, HeroPower


migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
