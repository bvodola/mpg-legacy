# Creates a dictionary, using the key/value pair as
# fields from the collection
def create_dict(collection, key,value):
	dict = {} # Create a new dictionary
	dict[getattr(collection,key)] = getattr(collection,value)