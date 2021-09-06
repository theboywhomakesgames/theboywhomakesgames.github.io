import os
import markdown2

testPost = open("./Pysi/Posts/p1.md")
content = testPost.read()
output = markdown2.markdown(content)

indexfile = open("./index.html", "w")
indexfile.write(output)
indexfile.close()
testPost.close()