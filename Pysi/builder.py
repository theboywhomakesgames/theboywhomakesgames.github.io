import os
from wrapper import wrap
from jinja2 import Template

homeFile = open("./home/home.html")
homeContent = homeFile.read()
homeFile.close()

wrap("../index.html", homeContent)

# grab every blog post and create the blog
post_names = []
for post_file in os.listdir("./blog"):
    if post_file.endswith(".html"):
        post = open(os.path.join("./blog", post_file))
        post_content = Template(post.read())
        post_module = post_content.module
        post.close()
        wrap("../blog/{name}".format(name=post_file), post_content.render())
        post_names.append((post_module.title, post_file))

# create the post list
blog_list = "<ul>"
for post, file_name in post_names:
    blog_list = blog_list +'<li><h2><a href="/blog/{file}">{p}</a></h2></li><hr>'.format(p=post, file=file_name)
blog_list = blog_list + "</ul>"
wrap("../blog.html", blog_list)

# TODO: relative path in header links when using wrapper
# Right now it works cause I copy pasted the essential css files in all directories!
