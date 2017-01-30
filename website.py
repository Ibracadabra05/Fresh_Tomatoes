from fresh_tomatoes import open_movies_page

class Movie(object):

	""" Movie class

	Attributes:
		title (str): Movie title.
		poster_image_url (str): Box art URL.
		trailer_youtube_url (str): Youtube link to the movie trailer. 
	"""

	def __init__(self, title, poster_image_url, trailer_youtube_url):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url


logan = Movie("Logan", \
	"http://t1.gstatic.com/images?q=tbn:ANd9GcRPoMqL1vglrh7OF_69pT8gYMYnYaq1r7WfPMcD587V9uOR_hW2", \
	"https://www.youtube.com/watch?v=DekuSxJgpbY")

transformers = Movie("Transformers: The Last Knight", \
	"http://cdn1-www.comingsoon.net/assets/uploads/gallery/transformers-the-last-knight-official-gallery/lastknight.jpg", \
	"https://www.youtube.com/watch?v=AntcyqJ6brc")

john_wick = Movie("John Wick: Chapter 2", \
	"http://t3.gstatic.com/images?q=tbn:ANd9GcREi1g3MgQ7DjKaVIiHssDQK09-mXKLq9t5NRKV4osuzElqxVnM", \
	"https://www.youtube.com/watch?v=ChpLV9AMqm4")


favorite_movies = [logan, transformers, john_wick]
open_movies_page(favorite_movies)