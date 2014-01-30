from osv import osv, fields
from datetime import *
from time import strptime
import math
import calendar

class res_partner(osv.osv):
    """
    OpenERP Model : Res Partner Information
    """

    _inherit = 'res.partner'    
    _columns = {
        'name_prefix':fields.many2one('config.preffix', 'Prefix'),
        'lastname':fields.char('Lastname', size=128),
        'firstname':fields.char('Firstname', size=128), 
        'middlename':fields.char('Middle Name', size=128),
        'name_sufix':fields.many2one('config.suffix', 'Sufix'),

        'photo':fields.binary('Photo'),
        'birthdate': fields.date('Birth Date'),
        'birthplace':fields.many2one('config.city', 'Birth Place'),

        'age': fields.function(_compute_age, method=True, type='integer', string='Age', store=True),
        'gender':fields.selection([
            ('M','Male'),
            ('F','Female'),
        ],'Gender'), 
        'height':fields.char('Height', size=64),
        'weight':fields.char('Weight', size=64),        
        'marital_status_id':fields.many2one('hr.employee.marital.status', 'Marital Status'),
        'mothers_maiden_name':fields.char('Mothers Maiden Name', size=128),   
        'religion_id':fields.many2one('config.religion', 'Religion', required=False),
        'tribe_id':fields.many2one('config.tribe', 'Tribe'),
        'spouse_id':fields.many2one('res.partner', 'Spouse', required=False),
        'educational_attainment':fields.many2one('config.education', 'Educational Attainment'),
        }
    _rec_name = "complete_name"    
    
    _defaults = {
        'citizenship_id' : 171,

    }
res_partner()

class res_partner_others(osv.osv):
    """
    OpenERP Model : Partner Other Information
    """
    _name='res_partner_others'
    _columns ={
               'partner_id':fields.many2one('res.partner', 'name', required=True),
               'is_deceased':fields.boolean('Deceased?'),
               'deceased_date':fields.date('Deceased Date'),
               }
    
    _defaults={
               'is_deceased':False,
               }
res_partner_others()

class res_partner_dependents(osv.osv):
    """
    OpenERP Model : Partner Dependents
    """
    _name='res_partner_dependents'
    _columns ={
               'partner_id':fields.many2one('res.partner', 'name', required=True),
               'dependent_id':fields.many2one('res.partner','name','Dependents', required=False),
               'relation':fields.selection([
                                            ('child','Childer'),
                                            ('parent','Parent'),
                                            ('relative','relative'),
                                            ('friend','Friend'),
                                            ('boarder','Boarder'),
                                            ('visit','Visitor'),
                                            ('other','Others'),
                                            ],'Relationship'),
               'date_start_reside':fields.date('Date Start of Residency',required=False),
               'date_end_reside':fields.date('Date End of Residency',required=False),
               'related_deceased': fields.related('dependent_id','is_deceased', type='many2one', relation='res.partner.others', string='Deceased?'),
               'related_deceased_date': fields.related('dependent_id','deceased_date', type='many2one', relation='res.partner.others', string='Deceased Date'),
               }
res_partner_dependents()
    
class res_partner_contact(osv.osv):
    """
    OpenERP Model : Partner Contacts
    """
    _name='res_partner_contact'
    _columns ={
               'partner_id':fields.many2one('res.partner', 'name', required=True),
               'contact':fields.char('contact', size=25, required=True),
               'contact_type':fields.selection([
                                                ('mobile','Mobile'),
                                                ('telno','Telephone'),
                                                ('email','Email'),
                                                ('sns','Social Network Service'),
                                                ],'Contact Type'),               
               'sns_id':fields.many2one('configsns', 'sns_name', required=True),
               'is_active':fields.boolean('Active'),
               'school_id':fields.many2one('config.school', 'name', required=True),
               'sy_graduated': fields.char('School Year Graduated',size=9),
               }
    
    _defaults={
            'is_active':True,
              }
res_partner_contact()
    
class res_partner_school_attended(osv.osv):
    """
    OpenERP Model : Partner School Attended
    """
    _name='res_partner_school_attended'
    _columns ={
               'partner_id':fields.many2one('res.partner', 'name', required=True),
               'education_level_id':fields.many2one('config.education', 'School Level'),
               'school_id':fields.many2one('config.school', 'name', required=True),
               'sy_graduated': fields.char('School Year Graduated',size=9),
               }
res_partner_school_attended()
    

class resident_information(osv.osv):
    """
    OpenERP Model : Resident Information
    """
    _name='resident_information'
    _columns ={
               'partner_id':fields.many2one('res.partner', 'name', required=True),
               'purok_id':fields.many2one('config.purok', 'purok_name', required=True),
               'house_no': fields.integer('House No.'),
               'block_no': fields.integer('Block No.'),
               'lot_no': fields.integer('Lot No.'),
               'house_type_id':fields.many2one('config.house_type', 'name', required=True),
               'is_partner_owner':fields.boolean('House is Owned?'),
               'owner_id':fields.many2one('res.partner', 'name', required=False),
               'date_start_reside':fields.date('Date Start of Residency',required=False),
               'date_end_reside':fields.date('Date End of Residency',required=False),
               'related_deceased': fields.related('partner_id','is_deceased', type='many2one', relation='res.partner.others', string='Deceased?'),
               'related_deceased_date': fields.related('partner_id','deceased_date', type='many2one', relation='res.partner.others', string='Deceased Date'),
               }
resident_information()
    
