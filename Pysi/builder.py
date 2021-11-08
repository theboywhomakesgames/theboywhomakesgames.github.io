import os

tagFile = open("./headers/headers.html")
tags = tagFile.read()
tagFile.close()

homeFile = open("./home/home.html")
homeContent = homeFile.read()
homeFile.close()

indexfile = open("../index.html", "w")

# start html
indexfile.write("\
    <!doctype html>\
    <html>\
")

# write tags
indexfile.write(tags)

# start body
indexfile.write("\
    <body>\
")

# read header
headerFile = open("./style/header.html")
headerContent = headerFile.read()
headerFile.close()
indexfile.write(headerContent)

indexfile.write(homeContent)

# read footer
footerFile = open("./style/footer.html")
footerContent = footerFile.read()
footerFile.close()
indexfile.write(footerContent)

# end of body
indexfile.write("\
    </body>\
")

# end html
indexfile.write("\
    </html>\
")
indexfile.close()
