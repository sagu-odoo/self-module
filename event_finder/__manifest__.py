{
    'name': "event_finder",
    'version': '1.1.0',
    'author': "sagu",
    'category': 'Event Finder',
    # data files always loaded at installation
    'data': [
         'security/ir.model.access.csv',
         'view/event_view.xml',
         'view/event_menues.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        
    ],
    'application': True,
    'installable': True,
    'auto_install':True,
    'license': 'LGPL-3',
}
