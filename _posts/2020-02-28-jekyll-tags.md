---
layout: post
title: Automated Jekyll blog tags
tags: [web, tutorial, jekyll]
description: How I implemented tags for this blog theme (no, they did not come with it)
---

This blog is built on the [Hyde](https://github.com/poole/hyde) theme for [Jekyll](https://jekyllrb.com/), a light framework for building static websites which uses the [Liquid](https://jekyllrb.com/docs/liquid/) templating language. It didn't come with blog tags, so I had to poke around and figure out how to implement them.

Since this blog is hosted on Github Pages, you can see all the code in [my public repo](https://github.com/rfong/rflog), but I figured a quick walkthrough post would be easier to navigate.


## Describing tags

One can describe arbitrary attributes within the metadata of a Jekyll post (or page, etc). I'm choosing to format the tag metadata as follows.

{% highlight markdown %}
---
layout: post
title: Automated Jekyll blog tags
tags: [web, jekyll, all-about-tags]
---

... Lorem ipsum dolor sit
{% endhighlight %}

Since tag names will eventually need to be in a URI-friendly format, I'm going to keep it super simple and stick with a tag naming convention of `[\w\d-]+` (alphanumeric characters and hyphens allowed) for my blog. If you want to support spaces and other characters, you could do it with URI encoding, but I decided not to.


## Displaying tags on posts/pages

I display the tags on each post by adding this snippet to the post template.
{% highlight liquid %}{% raw %}
<span class="post-tags">
  {% for tag in post.tags %}
    <a class="post-tag"
       href="{{ site.baseurl }}/tag/{{ tag | slugify }}"
       >{{ tag }}</a>{% unless forloop.last %}, {% endunless %}
  {% endfor %}
</span>
{% endraw %}{% endhighlight %}
- The `unless` clause delimits the tags by `, `, leaving off a trailing delimiter.
- Depending on what kind of Jekyll object you're pulling tags from (a post, a page, an include), you may need to use `post.tags`, `page.tags`, or `include.post.tags`.
- Regarding your `site.baseurl`, see notes at the end of the post about URL configuration.

In the Hyde theme, posts are described in two locations by default: `/_layouts/post.html`, which describes the layout of an individual blog post page, and `index.html`, which shows a page with multiple blog posts on it.

#### Handling posts with no tags

As written above, the `post-tags` div will appear empty on a post with no tags. However, if you're using a cute <i class="fas fa-tags"></i> icon like my blog does, you may want to hide this snippet when `tags` is empty.

Apparently you can't do a simple empty array check in Liquid; I had to resort to [this StackOverflow hack](https://stackoverflow.com/questions/16762714/how-can-i-compare-a-strings-size-length-in-jekylls-liquid-templates/16765331#16765331).

{% highlight liquid %}{% raw %}
{% capture difference %}
  {{ post.tags | size | minus:1 }}
{% endcapture %}
{% unless difference contains '-' %}
  <span class="post-tags">
    ...
  </span>
{% endunless %}
{% endraw %}{% endhighlight %}

#### I don't want to duplicate `post-tags` in multiple places

I wanted my posts to appear the same on individual pages or when aggregated into the index page, so I refactored Hyde's post display into a separate partial which I placed at `_includes/post.html`. Your mileage may vary based on your blog needs.

Again, if you're using an `_includes` partial, you will want to use `include.post.tags` in your template instead of `post.tags`.


## Auto-collecting tags across site

If you want to display all tags somewhere, you will first need to collect them from across your site, within the templating language. For this, I referenced [Codinfox's blog post](https://codinfox.github.io/dev/2015/03/06/use-tags-and-categories-in-your-jekyll-based-github-pages/) on how they implemented tags and categories in Jekyll.

This snippet is borrowed directly from Codinfox, but I'm duplicating it here for quick reference.
{% highlight liquid %}{% raw %}
---
layout: default
title: Tag
---

{% comment %}
=======================
The following part extracts all the tags from your posts and sort tags, so that you do not need to manually collect your tags to a place.
=======================
{% endcomment %}
{% assign rawtags = "" %}
{% for post in site.posts %}
  {% assign ttags = post.tags | join:'|' | append:'|' %}
  {% assign rawtags = rawtags | append:ttags %}
{% endfor %}
{% assign rawtags = rawtags | split:'|' | sort %}

{% comment %}
=======================
The following part removes dulpicated tags and invalid tags like blank tag.
=======================
{% endcomment %}
{% assign tags = "" %}
{% for tag in rawtags %}
  {% if tag != "" %}
    {% if tags == "" %}
      {% assign tags = tag | split:'|' %}
    {% endif %}
    {% unless tags contains tag %}
      {% assign tags = tags | join:'|' | append:'|' | append:tag | split:'|' %}
    {% endunless %}
  {% endif %}
{% endfor %}
{% endraw %}{% endhighlight %}

If you place it in `_includes`, it can now be included wherever you want to reference all site tags, such as in a sidebar.
{% highlight liquid %}{% raw %}
{% include collect_tags.html %}
{% for tag in tags %}
  <a class="post-tag"
     href="{{ site.baseurl }}/tag/{{ tag | slugify }}"
     >{{ tag }}</a>{% unless forloop.last %}, {% endunless %}
{% endfor %}
{% endraw %}{% endhighlight %}


## Tag categories

#### Displaying a tag page

I wrote a layout `_layouts/tagpage.html` to display all posts tagged with a certain tag.
{% highlight liquid %}{% raw %}
---
layout: default
---

<div class="post">
<h1>Tag: {{ page.tag }}</h1>

<div>
{% for post in site.posts %}
  {%comment%}
    According to documentation, arrays should be filterable
    with `where_exp`, but I couldn't get it to work.
    {%endcomment%}
  {% if post.tags contains page.tag %}
    {% include post_listing.html %}
  {% endif %}
{% endfor %}
</div>

</div>
{% endraw %}{% endhighlight %}

Jekyll does not support tag pages out of the box, and its official recommendation is that if you implement them, you should manually write a separate metadata file for each tag page.
{% highlight markdown %}
---
layout: tagpage
tag: jekyll
robots: noindex
---
{% endhighlight %}

I don't have the patience for that shit, so let's auto-generate them.

### Auto-generating tag pages

To do this, we'll need to collect all tags in our site and then output metadata for each in the format of the snippet above. Long Qian wrote a [Python script](https://github.com/qian256/qian256.github.io/blob/master/tag_generator.py) to do this, which they run manually before `git push`ing. I wanted a much more automated solution, so I used hooks. 

#### Jekyll hooks

Jekyll [hooks](https://jekyllrb.com/docs/plugins/hooks/) are Ruby functions which can be registered to run after certain events, such as when a post is saved to disk or rendered. They are a subtype of [plugins](https://jekyllrb.com/docs/plugins/installation/), which the build tool expects as `.rb` files in the `_plugins` directory.

My hook auto-runs on `:post_write` and calls a shell subprocess to run my Python script.
{% highlight ruby %}
# Filename: _plugins/compile_tags.rb
Jekyll::Hooks.register :posts, :post_write do
  system("python _plugins/compile_tags.py")
end
{% endhighlight %}

There are many disparate ways to launch a subprocess in Ruby. I used [this handy flowchart](https://stackoverflow.com/a/37329716/1006596) from StackOverflow to help me choose `system`.

#### Script to generate tag pages

My tag page generator script is more concise than Long Qian's, but basically has the same effect. It scrapes all tags and generates metadata files describing tag pages which are served at `tag/my-tag-name`.
{% highlight python %}
#!/usr/bin/env python
# Filename: __plugins/compile_tags.py

'''
This script generates tag pages for all your post tags for a 
Jekyll site. It is invoked from a plugin after post_write.
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
      # Find tags & cut them.
      if line.startswith('tags: '):
        all_tags += [
          t.strip() for t in line[len("tags: "):].split(',')]
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
{% endhighlight %}

(Also in Gist form [here](https://gist.github.com/rfong/9e7a9e99a1295deaa58f81548eaf66d6).)

That's all! Restart your Jekyll server to make sure you're using the new plugin, and you should see specs for tag pages generated into the `tag/` directory, which you can then link to in your post layouts as `{%raw%}{{site.baseurl}}/tag/{{tag}}{%endraw%}`.

Enjoy blogging :)

<hr>

## Debugging notes

### Not all URLs work

If your blog is serving from somewhere other than your domain root, e.g. serving from `https://me.github.io/blog/` rather than `https://me.github.io/`, double check that your theme uses its `site.baseurl` as expected. (`site.baseurl` is used to indicate the root folder of the Jekyll site. Confusingly named, there is also a `site.url` used to indicate your root domain; [here's](https://stackoverflow.com/a/27400343/1006596) a great StackOverflow explanation, and here's [a good blog post](https://byparker.com/blog/2014/clearing-up-confusion-around-baseurl/) on it.)

For this blog, I have the following set in my `_config.yml`.
```
url:              https://rfong.github.io
baseurl:          /rflog
```

#### Is the theme expecting an alternative `baseurl`?

The Hyde theme I'm using didn't seem to, so I did `git grep "site.baseurl"` to double check its usage.

Some generated Jekyll URLs, such as post URLs, are prepended with a slash, so you just need:
```{%raw%}
{{ site.baseurl }}{{ post.url }}
{%endraw%}```

For a manually written URL, you'll want to include the slash.
```{%raw%}
{{ site.baseurl }}/public/css/poole.css
{{ site.baseurl }}/tag/{{ tag | slugify }}
{%endraw%}```

I couldn't find whether Liquid had a readily available `os.path.join` equivalent, but you can just concat by smashing Liquid tags next to each other.
