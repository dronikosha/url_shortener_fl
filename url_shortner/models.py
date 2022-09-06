import random
import string

from url_shortner import db, domain


class URL(db.Model):
    __tablename__ = 'url'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(255), nullable=False)
    short_url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"URL('{self.url}', '{self.short_url}')"

    @staticmethod
    def generate_short_url():
        short = f'{domain}' + "/" + ''.join(random.choice(
            string.ascii_uppercase + string.digits) for _ in range(6))
        return short
