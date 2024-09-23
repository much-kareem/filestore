'''
Created on Nov 10, 2020

@author: Zuhair Hammadi
'''
from odoo import models, fields
from odoo.tools import config

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    attachment_location = fields.Selection([('s3', 'S3 Storage'), ('file', 'File System'), ('db', 'Database')], required = True, default = 'file', config_parameter='ir_attachment.location')
    aws_access_key_id = fields.Char()
    aws_secret_access_key = fields.Char()
    aws_region_name = fields.Char()
    aws_endpoint_url = fields.Char()
    
    aws_api_version = fields.Char()
    aws_use_ssl = fields.Boolean()
    aws_verify = fields.Char()
    
    s3_bucket = fields.Char()    
    s3_delete = fields.Boolean(config_parameter='ir_attachment.s3_delete', help='Delete s3 file when attachment deleted')
    s3_cache = fields.Boolean(config_parameter='ir_attachment.s3_cache', help='Cache in file system')
        
    def get_values(self):
        get_param = self.env['ir.config_parameter'].sudo().get_param
        
        res = super(ResConfigSettings, self).get_values()
        
        for fname in ['s3_bucket', 'aws_access_key_id', 'aws_secret_access_key', 'aws_region_name','aws_endpoint_url','aws_api_version','aws_use_ssl','aws_verify']:
            value = get_param('ir_attachment.%s' % fname) or config.get(fname)
            if self._fields[fname].type == 'boolean':
                value = bool(value)
            res[fname] = value
        
        return res
    
    
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        
        set_param = self.env['ir.config_parameter'].sudo().set_param
        
        for fname in ['s3_bucket', 'aws_access_key_id', 'aws_secret_access_key', 'aws_region_name','aws_endpoint_url','aws_api_version','aws_use_ssl','aws_verify']:
            value = self[fname]
            config_parameter = 'ir_attachment.%s' % fname
            if value == config.get(fname):
                set_param(config_parameter, False)
            else:
                set_param(config_parameter, value)
                