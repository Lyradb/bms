from osv import osv
from osv import fields

class config_sns(osv.osv):
    _name='config_sns'
    _columns ={
        'sns_init':fields.char('Popular Name', size=),
        'sns_name':fields.char('Full Name', size=25),
        'sns_website':fields.char('Website', size=25),
               }
config_education()

class config_education(osv.osv):
    _name='config_education'
    _columns ={
        'name':fields.char('Education Level', size=25),
               }
config_education()

class config_school(osv.osv):
    _name='config_school'
    _columns ={
        'school_name':fields.char('School Name', size=25),
        'school_init':fields.char('School Initial', size=10),
               }
config_education()

class config_prefix(osv.osv):
    _name='config_prefix'
    _columns ={
        'pref_code':fields.char('Prefix', size=8),
        'pref_desc':fields.char('Prefix Description', size=15),
               }
config_prefix()

class config_sufix(osv.osv):
    _name='config_prefix'
    _columns ={
        'suf_code':fields.char('Suffix', size=8),
        'suf_desc':fields.char('Sufix Description', size=15),
               }
config_sufix()

class config_sufix(osv.osv):
    _name='config_sufix'
    _columns ={
        'suf_code':fields.char('Suffix', size=8),
        'suf_desc':fields.char('Sufix Description', size=15),
               }
config_sufix()

class config_purok(osv.osv):
    _name='config_purok'
    _columns ={
        'purok_name':fields.char('Purok',size=25),
        'barangay_id':fields.one2many('config.barangay','Barangay'),
               }
config_purok()

class config_house_type(osv.osv):
    _name='config_house_type'
    _columns ={
        'name':fields.char('House Type',size=25),
               }
config_house_type()

class config_barangay(osv.osv):
    _name='config_barangay'
    _columns ={
        'barangay_name':fields.char('Barangay',size=25),
        'city_id':fields.one2many('config.city','Municipality/City'),
        'barangay_ids':fields.one2many('config.purok','barangay_id','Purok'),
               }
config_barangay()

class config_city(osv.osv):
    _name='config_city'
    _columns ={
        'city_name':fields.char('Municipality/City',size=25),
        'is_city':fields.boolean('City?'),
        'prov_id':fields.one2many('config.province','Province',required=False),
        'city_ids':fields.one2many('config.city','city_id','Municipality/City'),
               }
config_barangay()

class config_province(osv.osv):
    _name='config_province'
    _columns ={
        'prov_name':fields.char('Municipality/City',size=25),
        'prov_ids':fields.one2many('config.city','prov_id','Municipality/City'),
               }
config_province()