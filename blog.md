---
layout: page
title: Blog
permalink: /blog/
---

<ul class="post-list">
    {% for post in site.posts %}
      <li>
        <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}<!-- &mdash; <a href="{{ post.url | prepend: site.baseurl }}#disqus_thread"></a>--></span>

        <h2>
          <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
	  </h2>
  </li>
    {% endfor %}
</ul>

<script type="text/javascript">
/* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
var disqus_shortname = 'samwolfson'; // required: replace example with your forum shortname

/* * * DON'T EDIT BELOW THIS LINE * * */
(function () {
var s = document.createElement('script'); s.async = true;
s.type = 'text/javascript';
s.src = '//' + disqus_shortname + '.disqus.com/count.js';
(document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(s);
}());
</script>