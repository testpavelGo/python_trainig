from datetime import date

class Contact:
    def __init__(self, firstname, middlename, lastname, nickname, title, company, address, homephone, mobilephone,
                 email, bday, bmonth, byear, aday, amonth, ayear, group_name, address2, phone2, notes):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth =amonth
        self.ayear = ayear
        self.group_name = group_name
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
