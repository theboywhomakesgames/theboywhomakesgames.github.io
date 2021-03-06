import os
from jinja2 import Template

def wrap(outputAddress, pageContent):
    tagFile = open("./headers/headers.html")
    tags = Template(tagFile.read())
    tags = tags.render(bs_address="bs/css/bootstrap.min.css")
    tagFile.close()

    indexfile = open(outputAddress, "w")

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

    indexfile.write(pageContent)

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
