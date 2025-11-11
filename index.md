---
layout: default
title: "OM"
---

<style>
/* === Modern Blog Styling === */
body {
  font-family: 'Poppins', sans-serif;
  background-color: #fafafa;
  color: #222;
  margin: 0;
  padding: 0;
}

h1, h2, h3 {
  font-weight: 600;
  color: #111;
}

a {
  color: #0078ff;
  text-decoration: none;
  transition: color 0.3s ease;
}
a:hover {
  color: #005ec2;
  text-decoration: none;
}

.blog-header {
  text-align: center;
  padding: 60px 20px 40px 20px;
  background: linear-gradient(120deg, #0078ff, #00c6ff);
  color: #fff;
  border-radius: 0 0 40px 40px;
}

.blog-header h1 {
  font-size: 2.8rem;
  margin-bottom: 10px;
}

.blog-header p {
  font-size: 1.2rem;
  opacity: 0.9;
}

.post-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 30px;
  max-width: 1100px;
  margin: 50px auto;
  padding: 0 20px;
}

.post-card {
  background: #fff;
  border-radius: 20px;
  padding: 25px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.post-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.post-card h2 {
  font-size: 1.5rem;
  margin-top: 0;
}

.post-meta {
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 10px;
}

.post-excerpt {
  color: #333;
  font-size: 1rem;
  margin-bottom: 20px;
}

.btn {
  display: inline-block;
  background: #0078ff;
  color: #fff;
  padding: 10px 18px;
  border-radius: 10px;
  font-weight: 500;
  transition: background 0.3s ease;
}

.btn:hover {
  background: #005ec2;
  text-decoration: none;
}
</style>

<div class="blog-header">
  <h1>BOSS</h1>
  <p>Insights, tutorials, and stories to help you grow faster 🚀</p>
</div>

<div class="post-list">
  {% for post in site.posts %}
    {% if post.published %}
    <div class="post-card">
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}</p>
      <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 25 }}</p>
      <a href="{{ post.url | relative_url }}" class="btn">Read More</a>
    </div>
    {% endif %}
  {% endfor %}
</div>
