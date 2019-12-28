# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class cioperwalian(models.Model):
#     _name = 'cioperwalian.cioperwalian'


#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class MMPeriodePerwalian(models.Model):
    _name = 'cioperwalian.mmperiodeperwalian'
    _description = 'Periode Perwalian'
    _order = 'name, description asc'
    name = fields.Char("Kode Periode")
    description = fields.Text("Deskripsi Periode")
    
    
def default_current_date(self):
    return fields.Datetime.now()


class MMPerwalianBidangMinat(models.Model):
    _name = 'cioperwalian.mmperwalianbidangminat'
    _description = 'Bidang Minat Perwalian'    
    
    
class MMPerwalianFase(models.Model):
    _name = 'cioperwalian.mmperwalianfase'
    _description = 'Fase Perwalian'    


class MMPerwalianDosenWali(models.Model):
    _name = 'cioperwalian.mmperwaliandosenwali'
    _description = 'Dosen Perwalian'
    
class MTPerwalianSimple(models.Model):
    _name = 'cioperwalian.mtperwaliansimple'
    _description = 'Transaksi Data Perwalian'
    _order = 'namaMahasiswa, periodePerwalian, fasePerwalian asc'        
    name = fields.Char('Nama', default=None, index=True, help='Nama', readonly=False,required=True, translate=False,)
    periodePerwalian = fields.Selection([('1920_01', '1920 Gasal'), ('1920_02', '1920 Genap'), ('2021_01', '2021 Gasal'), ('2021_01', '2021 Genap')], 'Periode Perwalian', default=None, index=True, help='Nama Mahasiswa', readonly=False,required=True, translate=False,)
    fasePerwalian = fields.Selection([('krs', 'KRS'), ('pascauts', 'Pasca UTS'), ('prauas', 'Pra UAS'), ], 'Fase Perwalian', default=None, index=True, help='Fase Perwalian', readonly=False,required=True, translate=False,)
    taggalIsian = fields.Datetime('Tanggal Perwalian', default=lambda self: fields.Datetime.now())
    programStudi = fields.Selection([('s1si', 'S1 Sistem Informasi'), ('d3si', 'D3 Sistem Informasi'), ('s1ti', 'S1 Informatika')], 'Program Studi')
    dosenWali = fields.Selection([('iwwp', 'I Wayan Widi Pradnyana, S.Kom, MTI')], 'Nama Dosen Wali')
    namaMahasiswa = fields.Char('Nama Mahasiswa', default=None, index=True, help='Nama Mahasiswa', readonly=False,required=True, translate=False,)
    nimMahasiswa = fields.Char('NIM Mahasiswa')
    emailMahasiswa = fields.Char('Email Mahasiswa')
    hpMahasiswa = fields.Char('Nomor HP Mahasiswa')
    akunSosialMahasiswa = fields.Char('Akun Sosial Mahasiswa')
    ipkMahasiswa = fields.Float('IPK Terakhir Mahasiswa')
    ipsMahasiswa = fields.Float('IPS Terakhir Mahasiswa')
    kegiatanPeserta = fields.Text('Kegiatan Panitia')
    kegiatanPesertaFile = fields.Binary('File Kegiatan Panitia')
    academicPeriod = fields.Many2one('cioacademic.mmacademicperiod', string='Academic Period')

    
    @api.multi    
    def button_hello(self):        
        return True