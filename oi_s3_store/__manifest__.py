# -*- coding: utf-8 -*-
{
'name': 'Store Attachment on Amazon S3',
'summary': 'Amazon Connector, Amazon Storage Connector, S3 Connector, S3 Attachment, '
           'Attachment Connector, Amazon S3 Storage, Cloud Connector, Amazon Cloud',
'description': '''Store Attachment on Amazon S3 or S3 Compatible
        
    ''',
'author': 'Openinside',
'website': 'https://www.open-inside.com',
'license': 'OPL-1',
'price': 189.0,
'currency': 'USD',
'category': 'Extra Tools',
'version': '17.0.1.1.13',
'depends': ['base', 'mail'],
'data': ['data/ir_config_parameter.xml',
          'views/res_config_settings.xml',
          'data/ir_cron.xml',
          'views/ir_attachment.xml',
          'views/action.xml'],
'external_dependencies': {'python': ['boto3']},
'odoo-apps': True,
'images': ['static/description/cover.png'],
'application': False
}