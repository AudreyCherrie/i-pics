from django.conf.urls import url,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
url(r'^signup/',views.signup,name='signup'),
url(r'^$',views.home,from app import create_app,db
from flask_script import Manager,Server
from app.models import Writer,Subscribe,Post,Comments
from flask_migrate import Migrate,MigrateCommand

app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)
migrate =Migrate(app,db)
manager.add_command('db',MigrateCommand)
@manager.shell
def make_shell_context():
    return dict(app=app,db=db,Writer=Writer,Subscribe =Subscribe,Post=Post,Comments=Comments)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
name='Home',),
url(r'^timeline/',views.index,name='Index'),
url(r'^profile/(\d+)',views.first_profile,name='Profile'),
url(r'^images/',views.add_image,name='Image'),
url(r'^details/(\d+)',views.details,name='Details'),
url(r'^search/',views.search_profile, name='Search'),
url(r'^nav/(\d+)',views.nav,name='Nav'),
url(r'^comments/(\d+)',views.comment,name='Comment'),
url(r'^likes/(\d+)',views.like_post,name="like_post"),
url(r'^follow/(\d+)',views.follow,name="Follow"),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
