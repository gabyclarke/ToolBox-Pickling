""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
import pickle

def updateCounter(fileName, reset=False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		fileName: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be reset.
		returns: the new counter value

	>>> updateCounter('blah.txt',True)
	1
	>>> updateCounter('blah.txt')
	2
	>>> updateCounter('blah2.txt',True)
	1
	>>> updateCounter('blah.txt')
	3
	>>> updateCounter('blah2.txt')
	2
	"""
	if exists(fileName) and not reset:
		f = open(fileName, 'r+')
		content = int(pickle.load(f))
		content += 1
		f.seek(0,0)
		pickle.dump(content, f)
		f.close()
		return content

	else:
		f = open(fileName, 'w')
		pickle.dump('1', f)
		f.seek(0,0)
		f.close
		return 1


if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(updateCounter(sys.argv[1]))