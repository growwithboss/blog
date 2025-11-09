---
layout: default
title: "Browse by Tags"
permalink: /tags/
---

<h1>Tags</h1>
<ul>
{% assign all_tags = site.tags | sort %}
{% for tag in all_tags %}
  <li><a href="#{{ tag[0] }}">{{ tag[0] }}</a> ({{ tag[1].size }})</li>
{% endfor %}
</ul>

{% for tag in all_tags %}
  <h2 id="{{ tag[0] }}">{{ tag[0] }}</h2>
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}
