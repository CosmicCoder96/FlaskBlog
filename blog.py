from app import app, db
from app.models import User, Post

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post' :Post}