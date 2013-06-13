def read_input():
	"""docstring for read_input"""
	f = open('./text_justification_input.txt')
	return f.read()


def justify_text(text):
	"""takes a block of text, splits them into 'good' lines."""


if __name__ == '__main__':
	print justify_text(read_input())