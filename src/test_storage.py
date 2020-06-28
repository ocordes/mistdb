"""

written by: Oliver Cordes 2020-06-28
changed by: Oliver Cordes 2020-06-28

"""

import storage
import users


# make the output nicer
from colorama import Fore, Back, Style, init
import pyemoji as emo

# main
init(autoreset=True)

user = users.User('ocordes')

obj = storage.Storage()

id = obj.push('../files/textfile.txt', user)


print(Fore.GREEN + 'Done.'+emo.thumbsup)
