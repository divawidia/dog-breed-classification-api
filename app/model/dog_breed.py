from app import db

class DogBreed(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    breed = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    temperament = db.Column(db.String(100), nullable=True)
    popularity = db.Column(db.String(5), nullable=True)
    min_height = db.Column(db.Float(), nullable=True)
    max_height = db.Column(db.Float(), nullable=True)
    min_weight = db.Column(db.Float(), nullable=True)
    max_weight = db.Column(db.Float(), nullable=True)
    min_expectancy = db.Column(db.Integer(), nullable=True)
    max_expectancy = db.Column(db.Integer(), nullable=True)
    group = db.Column(db.String(100), nullable=True)
    grooming_frequency_value = db.Column(db.Float(), nullable=True)
    grooming_frequency_category = db.Column(db.String(100), nullable=True)
    shedding_value = db.Column(db.Float(), nullable=True)
    shedding_category = db.Column(db.String(100), nullable=True)
    energy_level_value = db.Column(db.Float(), nullable=True)
    energy_level_category = db.Column(db.String(100), nullable=True)
    trainability_value = db.Column(db.Float(), nullable=True)
    trainability_category = db.Column(db.String(100), nullable=True)
    demeanor_value = db.Column(db.Float(), nullable=True)
    demeanor_category = db.Column(db.String(100), nullable=True)
    
    def __repr__(self):
        return '<Message {}>'.format(self.name)