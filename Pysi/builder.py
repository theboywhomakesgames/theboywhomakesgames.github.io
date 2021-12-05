import os
from wrapper import wrap

homeFile = open("./home/home.html")
homeContent = homeFile.read()
homeFile.close()

wrap("../index.html", homeContent)

# grab every blog post and create the blog
post_names = []
for post_file in os.listdir("./blog"):
    if post_file.endswith(".html"):
        post = open(os.path.join("./blog", post_file))
        post_content = post.read()
        post.close()
        wrap("../blog/{name}".format(name=post_file), post_content)
        post_names.append(post_file)

# create the post list
blog_list = "<ul>"
for post in post_names:
    blog_list = blog_list + '<li><a href="/blog/{p}">{p}</a></li>'.format(p=post)
blog_list = blog_list + "</ul>"
wrap("../blog.html", blog_list)

# TODO: relative path in header links when using wrapper
