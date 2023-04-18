---
layout: page
title: Microblog
---

Daily journal snippets with less rhyme, reason, or polish.

<ul class="microblogs">
    {% for post in site.microblog reversed %}
    <li class="microblog-preview">
    	<a class="post-title" href="{{ site.baseurl }}{{ post.url }}">
	        <i class="post-date">{{post.date | date_to_string}}</i>
            {% if post.title and post.title != "" %}
                {{post.title}}
            {% else %} {%comment%} if no post title, use pathname after date {%endcomment%}
                {% assign splitName = post.name | split: "." | first | split: '-' %}
                {% assign nameLen = splitName | size | minus: 3 %}
                {{ splitName | slice: 3, nameLen | join: " " }}
            {% endif %}
        </a>
    </li>
    {% endfor %}
</ul>
