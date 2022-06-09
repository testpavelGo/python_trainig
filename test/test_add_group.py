# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="nnn", header="opo", footer="1234"))
    app.session.logout()

#only comment
def test_add_group_empty_parameters(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
