import app_factory
import dao

application = app_factory.get_app()

dao.db.init_app(application)
