import app_factory
import models

application = app_factory.get_app()

models.db.init_app(application)
