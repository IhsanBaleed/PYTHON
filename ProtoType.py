from abc import ABC, abstractmethod


class ProtoType(ABC): # inherit from ABC to enforce abstraction and prevent instances of the interface

    def __init__(self):
        self.id = 0
        self.name = ""
        print("Abstract Class Called")

    @abstractmethod
    def copy(self):
        pass

    def do_action(self):
        print (f"{self.name} is doing work using id= {self.id}")


class Alpha(ProtoType):

    a_static_id = 0

    def __init__(self, id_val):
        self.id = id_val
        self.name = f"Alpha Agent {self.id}"
        self.type = "Alpha"

        print("Made an Alpha Type")

    def copy(self):
        Alpha.a_static_id += 1
        c = Alpha(self.id + Alpha.a_static_id)
        return c


class Omega(ProtoType):

    o_static_id = 0

    def __init__(self, id_val):
        self.id = id_val
        self.name = f"Omega Agent {self.id}"
        self.type = "Omega"

        print("Made an Omega Type")

    def copy(self):
        Omega.o_static_id += 1
        c = Omega(self.id + Omega.o_static_id)
        return c


class Factory:

    def __init__(self):
        self.protos = [Omega(0), Alpha(100)]

    def clone_proto(self, p_type):

        if p_type == "Omega":
            return self.protos[0].copy()
        if p_type == "Alpha":
            return self.protos[1].copy()
        return


def test_prototype():
    #p = ProtoType()  # we enforced abstraction thanks to ABC class

    factory = Factory()

    o_proto = factory.clone_proto("Omega")
    o_proto.do_action()

    a_proto = factory.clone_proto("Alpha")
    a_proto.do_action()

    copies = []

    print ("Making copies")

    for i in range(2):
        copies.append(factory.clone_proto("Omega"))
        copies.append(factory.clone_proto("Alpha"))

    for copy in copies:
        copy.do_action()

