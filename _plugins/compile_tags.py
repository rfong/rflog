#!/usr/bin/env python

'''
This script generates tag pages for all your post tags for a Jekyll site.
It is invoked from a plugin after post_write.
Run it from the project root if testing.

Current convention expected for tag names is r/[-\w\d]+/
'''

import glob
import os

POST_DIR = '_posts/'
TAG_DIR = 'tag/'

# Collect all tags from all posts.
all_tags = []
for fname in glob.glob(POST_DIR + '*.md'):
  with open(fname, 'r') as f:
    for line in f:
      line = line.strip().replace('[', '').replace(']', '')
      # Find the line where tags are specified and cut tags.
      if line.startswith('tags: '):
        # TODO: To ensure consistency between blog tags and scraped
        # tag names, we should probably URI encode on both ends.
        all_tags += [t.strip() for t in line[len("tags: "):].split(',')]
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
