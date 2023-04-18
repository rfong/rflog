---
layout: post
title: Added a microblog to my blog
techTags: jekyll, bash
description: Jekyll-magic fun facts to spawn low-friction daily journal entries
---

My blog has a <a href="{{site.baseurl}}/microblog/">microblog</a> now!

The first week I ever did RC, I posted quick, unpolished journal entries without thinking about it too hard. As time slogged on, I inevitably polished my posts to be more and more explanatory and user-facing. As a result, my blog is pretty sparse.

Inspired by the ease of [Obsidian's daily notes plugin](https://help.obsidian.md/Plugins/Daily+notes), which simply spawns a new note titled with today's date, I implemented a similarly low-friction daily notes feature for my blog, and moved over my old unpolished journal entries to it.

# Jekyll "magic" wrangling

As a reminder, [Jekyll](https://jekyllrb.com/) is the Ruby-based blog-generation framework that [Github Pages](https://pages.github.com/) will auto-serve for you, and it's what I use to generate this blog.

There are multiple magic ways to create a new category of auto-collected blog posts in Jekyll. Two of the most relevant options in my case were "categories" and "collections".

I'm keeping these in scare quotes to emphasize that these are Jekyll terms that come bundled with magic Jekyll implications and effects, which get you running quickly but can also bite you in very confusing ways if you don't understand what they are doing under the hood. (Such a very Ruby approach.)

## 1. ["categories"](https://jekyllrb.com/docs/posts/#categories)

Create a new directory with a `_posts` subdirectory in it, e.g. `microblog/_posts`, and Jekyll will auto-collect any files matching its "post" detection rules.

The resulting ["posts"](https://jekyllrb.com/docs/posts/) (this is also a Jekyll Thing) will be collected into the superset of site posts, annotating `microblog` (or whatever you named your top-level directory) as a member of `post.categories`.

## 2. ["collections"](https://jekyllrb.com/docs/collections/)

Pages live in an underscore-prefixed folder, e.g. `_microblog`. They don't have to conform to Jekyll "post" rules.

This requires a small addition to your `_config.yml`.

```yaml
include: ["microblog"]
collections:
  microblog:
    output: true
    permalink: /:collection/:path/
```

Again, note that although the "collection" name is `microblog`, the directory name, `_microblog`, must be prefixed with an underscore. This is a Jekyll "magic" assumption.

I used "collections" rather than "categories" because, to minimize daily note friction, I wanted it to be ok to have daily note filenames that were simply the datestamp, e.g. `2023-04-18.md` and nothing else. Jekyll "posts" *must* include additional words in the filename, e.g. `2023-04-18-microblogging.md`.

# Spawning a new daily note

To minimize friction, I made a simple bash script that opens a new daily note, either titled simply with today's datestamp (`2023-04-18.md`), or with an optional addendum (`2023-04-18-another-note.md`) if needed for either deduplication or just for fun.

Not much of interest here, but here are a few bash fun facts.

- `date +"%Y-%m-%d"` to get the YYYY-MM-DD datestamp. More string formatting options can be found on the [`date` manpage](https://man7.org/linux/man-pages/man1/date.1.html).
- `if [ ! -z "$var" ]; then ... fi` to check if a variable is not empty.
- `if [ -f "$fname" ]; then ... fi` to check if a file already exists, although there are a few other ways to do this too. (If the file already exists, then I skip the file creation step and just open the note for editing.)



