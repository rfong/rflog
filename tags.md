---
layout: page
title: Tags
---

{% include collect_tags.html %}

<div class="tags">
  <i class="fa fa-tags"></i>
  {% for tag in tags %}
  <a href="{{ site.baseurl }}/tag/{{ tag | slugify }}">{{ tag }}</a>{% unless forloop.last %}, {% endunless %}
  {% endfor %}
</div>