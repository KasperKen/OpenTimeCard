import datetime


class Employee:

    def __init__(self, employeeID, firstName, lastName):
        self.employeeID = employeeID
        self.firstName = firstName
        self.lastName = lastName

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        self._attribute = value

    def fullName(self):
        return (f'{self.firstName} {self.lastName}')

    def clockIn(self):
        if Session.sessionExists(self.employeeID) == False:
            Session(self.employeeID)
        else:
            print('Error: Session for this employee already exists.')

    def clockOut(self):
        if Session.sessionExists(self.employeeID) == True:
            Session.terminateSession(self.employeeID)
        else: print("Error: No current session for this employee.")


class Session:

    sessions = {}

    def __init__(self, employeeID):
        self.employeeID = employeeID
        self.clockInTime = datetime.datetime.now()
        self.clockOutTime = ''
        self.__class__.sessions[employeeID] = self

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        self._attribute = value

    def sessionExists(employeeID):
       return employeeID in __class__.sessions

    def terminateSession(employeeID):
       __class__.sessions[employeeID].clockOutTime = datetime.datetime.now()
       with open('sessions.txt', 'w') as f:
           f.write(__class__.sessions[employeeID].employeeID)
           f.write(str(__class__.sessions[employeeID].clockInTime))
           f.write(str(__class__.sessions[employeeID].clockOutTime))
       del  __class__.sessions[employeeID]


employee = Employee('0001', 'John', 'Walker')
employee3 = Employee('0002', 'Mike', 'Milky')
employee.clockIn()
