#make a class -Art
class Art:

  def __init__(self,artist,title,medium,year, owner):
    self.artist=artist
    self.title=title
    self.medium=medium
    self.year=year
    self.owner=owner
  
  def __repr__(self):
    return '{name}. "{title}". {year}, {medium}. {owner}, {location}.'.format(name=self.artist, title=self.title, year=str(self.year), medium=self.medium, owner=self.owner.name, location=self.owner.location)

#create new Marketplace class

class Marketplace:
  def __init__(self):
    self.listings=[]

  #create add listing method
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  
  #create remove listing method
  def remove_listing(self, new_listing):
    self.listings.remove(new_listing)
  
  #create show listing method that goes through each listing and prints it out
  def show_listings(self):
    if self.listings==[]:
      print("There are no current listings")
    else:
      print("These are the current listings:")
      for listing in range(0,len(self.listings)):
        print(self.listings[listing])

#create main marketplace
veneer=Marketplace()

#test marketplace methods
#veneer.add_listing(girl_with_mandolin)
#veneer.remove_listing(girl_with_mandolin)
#veneer.show_listings()

#create client class
class Client:

  def __init__(self, name, location, is_museum):
    self.name=name
    self.location=location
    #location is name of museum, or Private collection if client is collector
    self.is_museum=is_museum

  #create sell artwork method:
  def sell_artwork(self,artwork, price):
    if artwork.owner==self:
      new_listing=Listing(artwork,price,self)
      veneer.add_listing(new_listing)
  
  #create buy artwork method:
  def buy_artwork(self,artwork):
    if artwork.owner!=self:
      for listing in range(0,len(veneer.listings)):
        if veneer.listings[listing].art==artwork:
          art_listing=veneer.listings[listing]
          artwork.owner=self
          veneer.remove_listing(art_listing)
  

#create first 2 clients Edytta Halpirt and MOMA
edytta=Client("Edytta Halpirt", "Private Collection", False)

moma=Client("The MOMA", "New York", True)

girl_with_mandolin=Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)

#test art class repr
#print(girl_with_mandolin)

#make listing class

class Listing:
  def __init__(self, art, price, seller):
    self.art=art
    self.price=price
    self.seller=seller

  def __repr__(self):
    return "{title}, {price}".format(title=self.art.title, price=self.price)


#Test  buy and sell artwork methods
edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")
veneer.show_listings()
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
veneer.show_listings()

#potential for future- add a wallet that affects dollar amount/buying power, add a wishlist, and create expiration dates for listings.