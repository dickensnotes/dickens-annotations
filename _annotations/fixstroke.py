import glob

import re

regex = r"stroke-width=\\\"(.*?)\\\""
for items in glob.glob('*.json'):
	if '-list.json' not in items:
		content = open(items).read()
		matches = re.finditer(regex, content)
		for x in matches:
			print(content.replace(x.group(), 'stroke-width=\"1\"'))
			content = content.replace(x.group(), 'stroke-width=\\"1\\"')
		with open(items, 'w') as f:
			f.write(content)