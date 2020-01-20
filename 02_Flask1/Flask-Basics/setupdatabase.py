from basic4_databases import db, Puppy

# Create all the tables (Models -> DB Tables)
db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)

# Should print None since not added to DB yet
print(sam.id)
print(frank.id)

db.session.add_all([sam, frank])
# db.session.add(sam)
# db.session.add(frank)

db.session.commit()

print(sam.id)
print(frank.id)