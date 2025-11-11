---
layout: default
title: "GrowWithBoss Blog"
---

<!-- GOOGLE FONTS -->
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">

<style>
/* GLOBAL */
body {
  font-family: 'Poppins', sans-serif;
  background: #fafafa;
  margin: 0;
  padding: 0;
  color: #222;
  line-height: 1.7;
}

a {
  text-decoration: none;
  color: #0078ff;
  transition: 0.3s ease;
}
a:hover {
  color: #005ec2;
}

/* HEADER */
.blog-header {
  text-align: center;
  padding: 70px 20px 50px 20px;
  background: linear-gradient(120deg, #0078ff, #00c6ff);
  color: #fff;
  border-radius: 0 0 40px 40px;
  margin-bottom: 50px;
}

.blog-header h1 {
  font-size: 2.8rem;
  font-weight: 600;
  margin-bottom: 10px;
}

.blog-header p {
  font-size: 1.2rem;
  opacity: 0.9;
  max-width: 700px;
  margin: 0 auto;
}

/* GRID OF POSTS */
.post-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 30px;
  max-width: 1150px;
  margin: 0 auto 60px auto;
  padding: 0 20px;
}

/* CARD */
.post-card {
  background: #fff;
  border-radius: 20px;
  padding: 28px;
  box-shadow: 0 5px 18px rgba(0,0,0,0.08);
  transition: all 0.25s ease;
}

.post-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 28px rgba(0,0,0,0.12);
}

.post-thumbnail {
  width: 100%;
  border-radius: 16px;
  margin-bottom: 18px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.07);
}

.post-card h2 {
  font-size: 1.4rem;
  margin: 0 0 10px 0;
  color: #111;
  font-weight: 600;
}

.post-meta {
  color: #666;
  font-size: 0.92rem;
  margin-bottom: 14px;
}

.post-excerpt {
  font-size: 1rem;
  color: #333;
  margin-bottom: 20px;
}

/* BUTTON */
.read-btn {
  display: inline-block;
  background: #0078ff;
  color: #fff;
  padding: 10px 18px;
  border-radius: 10px;
  font-weight: 500;
  transition: 0.3s;
}
.read-btn:hover {
  background: #005ec2;
}
</style>


<div class="blog-header">
  <h1>GrowWithBoss Blog</h1>
  <p>Insights, strategies, and ideas to help you grow smarter and faster.</p>
</div>

<div class="post-grid">
  {% for post in site.posts %}
    {% if post.published %}
    <div class="post-card">

      {% if post.thumbnail %}
        <img src="{{ post.thumbnail }}" class="post-thumbnail" alt="{{ post.title }}">
      {% endif %}

      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>

      <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}</p>

      <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>

      <a href="{{ post.url | relative_url }}" class="read-btn">Read More</a>
    </div>
    {% endif %}
  {% endfor %}
</div>
