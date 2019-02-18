# tmdbwrapper/post.py

class Post(object):
	def __init__(self, id):
		self.id = id

	def info(self):
		path = 'https://bazaar.com/api/v1/post/{}'.format(self.id)
		response = session.get(path)
		return response.json()

	@staticmethod
	def get(url, data):
		path = 'https://bazaar.com/api/v1/post'
		response = session.get(path)
		return response.json()
		