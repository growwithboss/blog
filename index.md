---
layout: default
title: "Grow With Boss Blog"
---

<h1>📝 Grow With Boss Blog</h1>

{% if site.posts and site.posts.size > 0 %}
  <ul class="post-list">
    {% for post in site.posts %}
      <li>
        <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
        <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}</p>
        {% if post.excerpt %}
          <p>{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
        {% endif %}
        <a href="{{ post.url | relative_url }}">Read more →</a>
      </li>
    {% endfor %}
  </ul>
{% else %}
  <p>No blog posts found yet.</p>
{% endif %}
