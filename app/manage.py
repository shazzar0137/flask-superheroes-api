from flask_migrate import Migrate
from app import app, db
from app.models import Hero, Power, HeroPower

# Important: move this line here so it's picked up when Flask loads the app
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
