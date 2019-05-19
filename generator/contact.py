import random
import string
from model.contact import Contact
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["help", "file"])
except getopt.GetoptError as err:
    usage()
    sys.exit(2)


n = 2
f = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="",
            lastname="",
            address="",
            homephone="",
            mobilephone="",
            workphone="",
            email="",
            email3="",
            address2="",
            secondaryphone="")] + [
    Contact(firstname=random_string("firstname", 10),
            lastname=random_string("lastname", 10),
            address=random_string("adress1", 30),
            homephone=random_string("111", 11),
            mobilephone=random_string("222", 11),
            workphone=random_string("333", 11),
            email=random_string("email1", 15),
            email3=random_string("email3", 10),
            address2=random_string("adress2", 25),
            secondaryphone=random_string("444", 15)
            )
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(testdata))
