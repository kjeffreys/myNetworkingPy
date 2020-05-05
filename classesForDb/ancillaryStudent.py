import ancillary as anc

class AncillaryStudent(anc.Ancillary):

    def __init__(self):
        anc.Ancillary.__init__(self)
        self.context = 'Students.' + self.context

