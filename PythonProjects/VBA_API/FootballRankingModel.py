from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

db = SQLAlchemy(app)


class FootballRanking(db.Model):
    __tablename__ = 'football_ranking'
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Wins = db.Column(db.Integer, nullable=False)
    Coach = db.Column(db.String(100))

    def json(self):
        return {
            'Id': self.Id,
            'Coach': self.Coach,
            'Wins': self.Wins,
            'Name': self.Name,
        }

    def __repr__(self):
        football_ranking_object = {
            'Id': self.Id,
            'Name': self.Name,
            'Wins': self.Wins,
            'Coach': self.Coach,
        }
        return json.dumps(football_ranking_object)

    def add_line(_name, _wins, _coach):
        new_team_line = FootballRanking(
            Name=_name,
            Wins=_wins,
            Coach=_coach
        )
        db.session.add(new_team_line)
        db.session.commit()

    def get_all_lines():
        return [FootballRanking.json(line) for line in FootballRanking.query.all()]


