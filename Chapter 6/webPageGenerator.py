#web page generator


def write_data(name, sentence):
    inline = open("webPage.html", "w")
    page = '\
    <html> \n \
        <head> \n \
        </head> \n \
        <body> \n \
            <center> \n \
            <h1>' + name + '</h1> \n \
            </center> \n \
            <hr/>' + sentence + '<hr/> \n \
        </body> \n \
    </html>'
    inline.write(page)
    inline.close()


def main():
    name = input('Enter your name: ')
    sentence = input('Write a sentence to describe yourself: ')
    write_data(name, sentence)


main()