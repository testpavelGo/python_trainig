# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="FFname", middlename="Mm name", lastname="Ll name", nickname="Nn",
                                title="title", company="comp",
                                address="addr 1",
                                homephone="+73258", mobilephone="+7123456789",
                                email="email@test.ei",
                                bday="7", bmonth="May", byear="1999",
                                aday="1", amonth="August", ayear="8888",
                                group_name="test_group",
                                address2="addr 2", phone2="homie",
                                notes=u"123\n%^&\nйцук\nqwert"))
    app.session.logout()
