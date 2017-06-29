# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution - module extension
#    Copyright (C) 2010- O4SB (<http://openforsmallbusiness.co.nz>).
#
##############################################################################

# noinspection PyStatementEffect
{
    'name': 'Pricelist Extensions',
    'version': '10.0.1.0.0',
    'category': '',
    'author': 'O4SB',
    'website': 'http://www.openforsmallbusiness.co.nz',
    'depends': ['product', 'sale'],
    "description": """
    This module implements many2many product ids for pricelist rules and provides
    a report for checking pricelist rules.
    """,
    'data': ['views/product_pricelist_view.xml',
             'views/product_price_category_view.xml',
             'security/ir.model.access.csv'
    #               'report/pricelist_report.xml'
    ],
    'installable': True,
    'active': False,
}
