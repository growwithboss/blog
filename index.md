---
layout: default
title: "BOSS BLOG"
---

<section style="text-align:center; margin-top:2rem;">
  <h1 style="font-size:2.2rem;">📝 BLOG </h1>
  <p style="color:#666; max-width:600px; margin:0 auto;">Sharing insights, guides, and lessons from my journey to grow smarter, faster, and stronger.</p>
</section>

<ul class="post-list">
  {% for post in site.posts %}
    <li>
      {% if post.thumbnail %}
        <img src="{{ post.thumbnail }}" alt="{{ post.title }}" style="width:100%; border-radius:12px; margin-bottom:1rem;">
      {% endif %}
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}</p>
      {% if post.excerpt %}
        <p>{{ post.excerpt | strip_html | truncatewords: 25 }}</p>
      {% endif %}
      <a class="btn" href="{{ post.url | relative_url }}">Read More</a>
    </li>
  {% endfor %}
</ul>
