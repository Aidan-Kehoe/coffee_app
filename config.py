import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'idontknowwhatthisisfor'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		"postgresql:///users_dev"
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	POSTS_PER_PAGE = 3
	ORIGINS = [('Brazil','Brazil'), ('Burundi','Burundi'), ('China','China'), ('Colombia','Colombia'),('Costa Rica', 'Costa Rica'), ('Cote d?Ivoire',"Cote d'Ivoire"),
	   ('Ecuador','Ecuador'), ('El Salvador','El Salvador'), ('Ethiopia','Ethiopia'), ('Guatemala','Guatemala'), ('Haiti','Haiti'), ('Honduras','Honduras'),
	   ('Indonesia','Indonesia'), ('Japan','Japan'), ('Kenya','Kenya'), ('Laos','Laos'), ('Malawi','Malawi'), ('Mexico','Mexico'), ('Myanmar','Myanmar'),
	   ('Nicaragua','Nicaragua'), ('Panama','Panama'), ('Papua New Guinea','Papua New Guinea'), ('Peru','Peru'), ('Philippines','Philippines'),
	   ('Rwanda','Rwanda'), ('Taiwan','Taiwan'), ('Tanzania, United Republic Of','Tanzania'), ('Thailand','Thailand'),
	   ('Uganda','Uganda'), ('United States','United States'), ('United States (Puerto Rico)','Puerto Rico'), ('Vietnam','Vietnam'),
	   ('Zambia','Zambia')]
	PROCESS = [('Natural / Dry', 'Natural'), ('Other', 'Other'), ('Pulped natural / honey', 'Honey'), ('Semi-washed / Semi-pulped', 'Semi-Washed'), ('Washed / Wet', 'Washed')]
