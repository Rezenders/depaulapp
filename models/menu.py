# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('DePaul-', SPAN('iD'), 'Lab'), XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href="https://depaulidlab.com/",
                  _id="depaul_logo")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# -----------------i-----------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    ('GitHub', False, 'https://github.com/gus9182/global-project-2018-1'),
]

DEVELOPMENT_MENU = False


# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------

def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # ------------------------------------------------------------------------------------------------------------------
    response.menu += [
        (T('My Sites'), False, URL('admin', 'default', 'site')),
        (T('This App'), False, '#', [
            (T('Design'), False, URL('admin', 'default', 'design/%s' % app)),
            LI(_class="divider"),
            (T('Controller'), False,
             URL(
                 'admin', 'default', 'edit/%s/controllers/%s.py' % (app, ctr))),
            (T('View'), False,
             URL(
                 'admin', 'default', 'edit/%s/views/%s' % (app, response.view))),
            (T('DB Model'), False,
             URL(
                 'admin', 'default', 'edit/%s/models/db.py' % app)),
            (T('Menu Model'), False,
             URL(
                 'admin', 'default', 'edit/%s/models/menu.py' % app)),
            (T('Config.ini'), False,
             URL(
                 'admin', 'default', 'edit/%s/private/appconfig.ini' % app)),
            (T('Layout'), False,
             URL(
                 'admin', 'default', 'edit/%s/views/layout.html' % app)),
            (T('Stylesheet'), False,
             URL(
                 'admin', 'default', 'edit/%s/static/css/web2py-bootstrap3.css' % app)),
            (T('Database'), False, URL(app, 'appadmin', 'index')),
            (T('Errors'), False, URL(
                'admin', 'default', 'errors/' + app)),
            (T('About'), False, URL(
                'admin', 'default', 'about/' + app)),
        ]),
        (T('Community'), False, None, [
            (T('Groups'), False,
             'http://www.web2py.com/examples/default/usergroups'),
            (T('Twitter'), False, 'http://twitter.com/web2py'),
            (T('Live Chat'), False,
             'http://webchat.freenode.net/?channels=web2py'),
        ]),
    ]


def manager_menu():
    try:
        if auth.has_membership(auth.id_group('Managers'), auth.user.id) or auth.has_membership(auth.id_group('Upper Managers'), auth.user.id)  :
            response.menu += [
                ('User Admin', False, '#', [
                 ('View Users', False, URL('depaulapp', 'users', 'show_all')),
                 ('Add Students', False, URL('depaulapp', 'users', 'add_student')),
                 ]),
                ('TimeReporting', False, '#', [
                 ('View Students Hours', False, URL('depaulapp','timereporting', 'ViewStudentHours')),
                 ]),
                ('Workscheduling', False, '#', [
                 ('View Students Hours', False, URL('depaulapp', 'workscheduling', 'show_hours')),
                 ]),
            ]
    except(AttributeError):
        pass

def student_menu():
    try:
        if auth.has_membership(auth.id_group('Students'), auth.user.id):
            response.menu += [
                ('TimeReporting', False, '#', [
                 ('Add Hours', False, URL('depaulapp', 'timereporting', 'AddHours')),
                 ('View Hours', False, URL('depaulapp', 'timereporting', 'ViewHours')),
                 ]),
                ('WorkScheduling', False, '#', [
                 ('Add Hours', False, URL('depaulapp', 'workscheduling', 'timereport')),
                 ('View Hours', False, URL('depaulapp', 'workscheduling', 'show_hours_student')),
                ]),
            ]
    except(AttributeError):
        pass

manager_menu()
student_menu()

if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()
