from apiwrapper import Post

get_req = Post.popular()

for value in enumerate(get_req['results'], start=1):
	print("{num}. {name} - {pop}".format(num=number, name=show['name'], pop=show['popularity']))