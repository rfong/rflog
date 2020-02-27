#!/usr/bin/env python

'''
This script generates tag pages for all your post tags for a Jekyll site.
It is invoked as a side effect of a plugin after post_write.
Run it from the project root.
'''

import glob
import os
import re

POST_DIR = '_posts/'
TAG_DIR = 'tag/'

# Collect all tags from all posts.
all_tags = []
for fname in glob.glob(POST_DIR + '*.md'):
	with open(fname, 'r') as f:
		for line in f:
			line = line.strip().strip('[]')
			# Find the line where tags are specified.
			if line.startswith('tags: '):
				# Clean string. All non-alphanumeric characters replaced with '-'.
				all_tags += [
					re.sub(r'[^\w\d]', '-', t)[1:]
					for t in line[len("tags: "):].split(',')]
				break
all_tags = sorted(list(set(all_tags)))

# Remove old tag pages
old_tags = glob.glob(TAG_DIR + '*.md')
for tag in old_tags:
  os.remove(tag)
 
# Create tag directory if it does not exist 
if not os.path.exists(TAG_DIR):
  os.makedirs(TAG_DIR)

# Write new tag pages.
TAG_PAGE_TEMPLATE = '''---
layout: tagpage
tag: {tag}
robots: noindex
---'''
for tag in all_tags:
	with open(TAG_DIR + tag + '.md', 'a') as f:
		f.write(TAG_PAGE_TEMPLATE.format(tag=tag))
