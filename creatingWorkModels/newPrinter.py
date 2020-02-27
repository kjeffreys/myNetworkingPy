'''
Create the python representation of the printer.

This will be sent to another function to transform
into specifically iPrint printer. May want to have the intermediate representation as just the info for other purposes.
'''
class Printer:

    def __init__(self, school, model, room, ip):
        self.school = school
        self.model = model
        self.room = room
        self.ip = ip
        self.name = self.school.upper() + '-' + self.model + '-' + self.room

class EldPrinter(Printer):
    
    def __init__(self, model, room, ip):
        Printer.__init__(self, 'Eld', 'HPm402', '90', '10.247.56.')
        self.model = model
        self.room = room
        self.ip = '10.247.56.' + ip
        self.name = self.school.upper() + '-' + self.model + '-' + self.room

'''
newPrinter = EldPrinter('m402', '200','100')
print('Print newPrinter call: {}'.format(newPrinter))
print()
for el in dir(newPrinter):
    if not el.startswith('__'):
        print(el)
print('New Printer name in caps: {}'.format(newPrinter.name))
print('New printer ip: {}'.format(newPrinter.ip))
'''

'''
# Best iter loop of keys/values I've found
>>> for k, v in vars(fle06).items():
...     print(k, v)
...
school Fle
model m402dne
room 06
ip 10.247.41.6
name FLE-m402dne-06
'''

