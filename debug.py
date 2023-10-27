import ipdb
from lib import *

# Test your code below...

iago = Role("Iago")
othello = Role("Othello")

act1 = Actor("Patrick Stewart")
act2 = Actor("Jack Black")
act3 = Actor("Hugh Jackman")
act4 = Actor("Nick Offerman")
act5 = Actor("Will Ferrell")

aud1 = Audition("Los Angeles", iago, act2)
aud2 = Audition("London", othello, act1)
aud3 = Audition("Los Angeles", iago, act5)
aud4 = Audition("Los Angeles", othello, act4)
aud5 = Audition("Syndey", othello, act3)
aud6 = Audition("Los Angeles", othello, act5)
aud7 = Audition("London", iago, act1)

# the below line allows us to stop & try stuff!
ipdb.set_trace()