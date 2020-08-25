import app_factory
import dao
import login

application = app_factory.get_app()

dao.db.init_app(application)

login.login_manager.init_app(application)
