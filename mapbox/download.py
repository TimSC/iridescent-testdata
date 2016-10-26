
import urllib2, os

if __name__=="__main__":

	print "Access token?"
	accessToken = raw_input()

	zoom = 12
	for x in range(2033, 2039):
		for y in range(1371, 1378):

			url = "https://api.mapbox.com/v4/mapbox.mapbox-streets-v7/{0}/{1}/{2}.vector.pbf?access_token={3}".format(zoom, x, y, accessToken)
			print url
			conn = urllib2.urlopen(url)
			dat = conn.read()
			pth = os.path.join(str(zoom), str(x))
			if not os.path.exists(pth):
				os.makedirs(pth)

			fi = open(os.path.join(pth, str(y)+".vector.pbf"), "wb")
			fi.write(dat)
			fi.close()

