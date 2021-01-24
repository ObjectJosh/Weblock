###########################
##### Website Class #######
###########################

class Website:
    # website class holds website links and the regular name, also acts as a Node
    # ie "www.facebook.com" and Facebook
    # websiteName is the "key" and the websiteLink is the "item"
    def __init__(self, websiteName, websiteLink, next=None, prev=None):
        self.link = websiteLink
        self.name = websiteName
        self.next = next
        self.prev = prev

    # other is another Website class, allows for sorting by alphabetical order
    def __lt__(self, other):
        return self.name < other.name

    def getName(self):
        return self.name

    def getLink(self):
        return self.link
