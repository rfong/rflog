---
layout: page
title: Microblog
---

Daily journal snippets with less rhyme, reason, or polish.

<ul class="microblogs">
    {% for post in site.categories.microblog %}
    <li class="microblog-preview">
	    <i class="post-date">({{post.date | date_to_string}})</i>
	    <a class="post-title" href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a>
    </li>
    {% endfor %}
</ul>
