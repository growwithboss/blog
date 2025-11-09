---
layout: home
title: "Grow With Boss Blog"
---

# 📝 Grow With Boss Blog

Welcome to **Grow With Boss** — your hub for insights, growth strategies, and ideas.

Explore the latest posts below 👇

{% for post in site.posts %}
  <article>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    <p><small>{{ post.date | date: "%B %d, %Y" }}</small></p>
    <p>{{ post.excerpt | strip_html | truncate: 160 }}</p>
    <hr>
  </article>
{% endfor %}
