from server.app import app
from server.extensions import db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance


with app.app_context():
    print("Seeding ... 🌱")

    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    User.query.delete()

  
    u1 = User(username="admin")
    u1.set_password("password")
    u2 = User(username="host")
    u2.set_password("secret")
    db.session.add_all([u1, u2])

    
    g1 = Guest(name="Emma Stone", occupation="Actor")
    g2 = Guest(name="Trevor Noah", occupation="Comedian")
    g3 = Guest(name="Serena Williams", occupation="Athlete")
    db.session.add_all([g1, g2, g3])

    e1 = Episode(date="2025-06-20", number=101)
    e2 = Episode(date="2025-06-21", number=102)
    db.session.add_all([e1, e2])
    db.session.commit()  

    a1 = Appearance(rating=5, guest_id=g1.id, episode_id=e1.id)
    a2 = Appearance(rating=4, guest_id=g2.id, episode_id=e1.id)
    a3 = Appearance(rating=3, guest_id=g3.id, episode_id=e2.id)
    db.session.add_all([a1, a2, a3])

    db.session.commit()
    print("Done! ✅")
