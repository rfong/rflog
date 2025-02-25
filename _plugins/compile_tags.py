#!/usr/bin/env python
# This script generates tag pages for all your post tags for a Jekyll site.
# It is invoked from a plugin after post_write.
# Run it from the project root if testing.
# Current convention expected for tag names is r/[-\w\d]+/

import glob
import itertools
import os

POST_DIRS = ['_posts/', '_microblog/']
TAG_DIR = 'tag/'
TAG_TYPES = ['techTags', 'tags']
FRONT_MATTER_DIVIDER = '---'

def main():
  # Collect all tags from all posts.
  all_tags = []
  filenames = itertools.chain.from_iterable(
      glob.glob(dirname+'*.md') for dirname in POST_DIRS)
  for fname in filenames:
    with open(fname, 'r') as f:
      seen_divider = False
      for line in f:
        # quit once we're done with the front matter
        if line == FRONT_MATTER_DIVIDER:
          # all done
          if seen_divider:
            break
          # just saw the first one
          seen_divider = True

        line = line.strip().replace('[', '').replace(']', '')

        # Find the lines where tags are specified and cut tags.
        for tag_type in TAG_TYPES:
          if line.startswith(tag_type + ': '):
            # TODO: To ensure consistency between blog tags and scraped
            # tag names, we should probably URI encode on both ends.
            all_tags += [t.strip() for t in line[len(tag_type+ ": "):].split(',')]

  all_tags = sorted(t for t in list(set(all_tags)) if len(t)>0)

  # Remove old tag pages
  old_tags = glob.glob(TAG_DIR+ '*.md')
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

main()
