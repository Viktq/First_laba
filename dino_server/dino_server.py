 #!/usr/bin/env python

from __future__ import print_function

from dino.srv import dino_service , dino_serviceResponse
import rospy
import random
from std_msgs.msg import String

_answer = "D"

def dinomancy(req):

    dino_suf = ["saurus", "raptor", "pteryx", "stacator", "rex",
                "ceratops", "gnathus", "roides", "draco", "dromeus"]

    dino_family = ["Abelisauridae", "Noasauridae", "Megalosauridae", "Carcharodontosauridae",
                   "Tyrannosauridae", "Plateosauridae", "Brachiosauridae", "Titanosauridae",
                   "Scelidosauridae", "Ankylosauridae", "Hadrosauridae", "Protoceratopsidae",
                   "Alvarezsauridae", "Cetiosauridae", "Diplodocidae", "Euhelopodidae",
                   "Nodosauridae", "Ceratopsidae", "Omeisauridae", "Vulcanodontidae"]

    dino_period = ["Early", "Middle", "Late"]

    dino_name = req.word
    _answer = dino_name.capitalize() + random.choice(dino_suf)
    print("Returning " + _answer)
    print(_answer + " belonged to the " + random.choice(dino_family) +
    " family and lived in the " + random.choice(dino_period) + " Triassic")

    pub = rospy.Publisher('chatter', String, queue_size=10)
    pub_str = _answer
    pub.publish(pub_str)
    return dino_serviceResponse(_answer)

def dino_service_server():
    rospy.init_node('dino_service_server')
    s = rospy.Service('dino_service', dino_service, dinomancy)
    print("Ready to dinomant")


if __name__ == "__main__":
    dino_service_server()
    rospy.spin()
