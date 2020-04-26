import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime as dt
Base = declarative_base()

class Canteen(Base):
	__tablename__ = 'canteens'
	id = db.Column(db.Integer, primary_key=True)
	ProviderID = db.Column(db.Integer, db.ForeignKey('providers.id'))
	Name = db.Column(db.String)
	Location = db.Column(db.String)
	time_open = db.Column(db.types.Time)
	time_closed = db.Column(db.types.Time)
	
	
	def __repr__(self):
		return "<Canteen(name='%s', location='%s', time_open='%s', time_closed='%s')>" % (
				self.Name, self.Location, self.time_open, self.time_closed)
	
class Provider(Base):
	__tablename__ = 'providers'
	id = db.Column(db.Integer, primary_key=True)
	ProviderName = db.Column(db.String)
	
	def __repr__(self):
		return "<Provider(name='%s')>" % self.ProviderName
	

canteens = [Canteen(id=1, Name='ESS building canteen', ProviderID=1, Location='Akadeemia tee 3 SOC-building', time_open=dt.time(8,30), time_closed=dt.time(18,30)),
		  Canteen(id=2, Name='Library canteen', ProviderID=1, Location='Akadeemoia tee 1/Ehitajate tee 7', time_open=dt.time(8,30), time_closed=dt.time(19)),
		  Canteen(id=3, Name='Main building Deli cafe', ProviderID=2, Location='Ehitajate tee 5 U01 building', time_open=dt.time(9), time_closed=dt.time(16,30)),
		  Canteen(id=4, Name='Main building Daily lunch restaurant', ProviderID=2, Location='Ehitajate tee 5 U01 building', time_open=dt.time(9), time_closed=dt.time(16)),
		  Canteen(id=5, Name='U06 building canteen', ProviderID=1, Location='U06 building', time_open=dt.time(9), time_closed=dt.time(16)),
		  Canteen(id=6, Name='Natural science buiding canteen',ProviderID=2, Location='Akadeemia tee 15 SCI building', time_open=dt.time(9), time_closed=dt.time(16)),
		  Canteen(id=7, Name='ICT building canteen', ProviderID=2, Location='Raja 15/Mäepealse 1', time_open=dt.time(9), time_closed=dt.time(16)),
		  Canteen(id=8, Name='Sports building canteen', ProviderID=3, Location='Männiliiva 7 S01 building', time_open=dt.time(11), time_closed=dt.time(20))
		  ]

providers = [Provider(id=1, ProviderName="Rahva Toit"),
			Provider(id=2, ProviderName="Baltic Restaurants Estonia AS"),
			Provider(id=3, ProviderName="TTU Sport"),
			Provider(id=4, ProviderName="BitStop Kohvik OU")
			]
			
engine = db.create_engine('sqlite:///./diners.db', echo=False)
Base.metadata.create_all(engine)

if __name__ == "__main__":
	#add data to tables
	Session = sessionmaker(bind=engine)
	session = Session()		
	session.add_all(canteens)
	session.add_all(providers)
	
	#add itc canteen
	itc = Canteen(Name='bitStop KOHVIK', ProviderID=4, Location="Raja 4C", time_open=dt.time(9,30), time_closed=dt.time(16));
	session.add(itc)
	session.commit()
	
	#canteens which are open 16.15-18.00
	print("Canteens open from 16.15 to 18.00:")
	for row in session.query(Canteen).filter(Canteen.time_open <= dt.time(16,15)).filter(Canteen.time_closed >= dt.time(18)).all():
		print(row.Name)
	
	#canteens which are serviced by Rahva Toit
	print("Canteens serviced by Rahva Toit:")
	for row in session.query(Canteen).join(Provider).filter(Provider.ProviderName=="Rahva Toit").all():
		print(row.Name)
	
	#delete data
	Canteen.__table__.drop(engine)
	Provider.__table__.drop(engine)
	
	#close database
	session.close()
