from odoo import models, fields, api
from datetime import datetime

class HistoriaClinica(models.Model):
    _name = 'medi_serv.historia_clinica'
    _description = 'Historia Clínica'

    cod_historia = fields.Char(string='Código Historia')

    # Datos del paciente
    id_pac = fields.Many2one('medi_serv.paciente', string='Paciente')
    nomb_pac = fields.Char(related='id_pac.name', string='Nombre del Paciente')
    fecha_nacimiento = fields.Date(related='id_pac.fecha_nacimiento', string='Fecha de Nacimiento')
    direccion_pac = fields.Char(related='id_pac.direccion', string='Dirección')
    telefono_pac = fields.Char(related='id_pac.telefono', string='Teléfono')
    edad_pac = fields.Integer(related='id_pac.edad', string='Edad')

    # Datos de atención
    nomb_med = fields.Many2one('medi_serv.medico', string='Médico')
    espec_med = fields.Selection(related='nomb_med.especialidad', string='Especialidad')
    sede_med = fields.Char(related='nomb_med.sede', string='Sede')
    fech_apertura = fields.Datetime(string='Fecha Apertura')
    fech_cierre = fields.Datetime(string='Fecha Cierre')
    fech_impresion = fields.Date(string='Fecha de Impresión', default=fields.Date.context_today)

    # Datos del acompañante
    nomb_acompanante = fields.Char(related='id_pac.nombre_acompanante',string='Nombre del Acompañante')
    tel_acompanante = fields.Char(related='id_pac.telefono_acompanante',string='Teléfono del Acompañante')
    parent_acompanante = fields.Char(related='id_pac.parentezco_acompanante',string='Parentesco')

    # Motivo de la consulta
    motivo_consulta = fields.Text(string='Motivo de la Consulta')
    descripcion_consulta = fields.Text(string='Descripción Consulta')

    # Antecedentes Patológicos
    arritmia = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Arritmia')
    autoinmunes = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Autoinmunes')
    cancer = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Cáncer')
    enf_cardiovascular = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Enfermedad Cardiovascular')
    infarto = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Infarto del Miocardio')
    insuf_card = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Insuficiencia Cardíaca')
    emergencia_hip = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Emergencia Hipertensiva')

    # Antecedentes Quirúrgicos
    ant_quir_desc = fields.Text(string='Descripción Quirúrgica')
    ant_quir_fecha = fields.Date(string='Fecha Quirúrgica')

    # Antecedentes Traumatológicos
    ant_trauma_desc = fields.Text(string='Descripción Traumatológica')
    ant_trauma_fecha = fields.Date(string='Fecha Traumatológica')

    # Transfusiones
    ant_transf_desc = fields.Text(string='Descripción Transfusiones')
    ant_transf_fecha = fields.Date(string='Fecha Transfusiones')

    # Alergias
    ant_alerg_desc = fields.Text(string='Descripción Alergias')
    ant_alerg_fecha = fields.Date(string='Fecha Alergias')

    # Farmacológicos
    ant_farma_desc = fields.Text(string='Descripción Farmacológicos')
    ant_farma_fecha = fields.Date(string='Fecha Farmacológicos')

    # Gino-Obstétricos
    menarquia = fields.Char(string='Menarquia')
    ciclos_menstrual = fields.Char(string='Ciclos Menstruales')
    autoexam_mama = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Autoexamen Mamario')
    inicio_rel_sex = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Inicio Relaciones Sexuales')
    activ_sex = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Actividad Sexual')
    num_companeros = fields.Char(string='N° de Compañeros Sexuales')
    met_planific = fields.Char(string='Método de Planificación')
    observaciones_gino = fields.Text(string='Observaciones')

    # Antecedentes Familiares
    hta_fam = fields.Char(string='Hipertensión (Pariente)')
    ca_prostata = fields.Char(string='Cáncer de Próstata (Pariente)')
    diabetes_fam = fields.Char(string='Diabetes (Pariente)')
    ca_colon = fields.Char(string='Cáncer de Colon (Pariente)')
    otro_cancer = fields.Char(string='Otro Tipo de Cáncer')
    otros_antec_fam = fields.Text(string='Otros Antecedentes Familiares')

    # Hábitos saludables
    bajo_sal = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Bajo Consumo de Sal')
    toma_antihip = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Toma Antihipertensivos')
    act_fisica = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Actividad Física >30min')
    bajo_grasa = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Bajo Consumo de Grasas')
    azucar_alta = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Eventos de Azúcar Alta')
    rica_fibra = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Consumo de Fibra')
    peso_adecuado = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Peso Adecuado')
    toma_agua = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Toma Agua')
    frutas_verduras = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Consume Frutas/Verduras')
    duerme_8h = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Duerme 8h')

    # Hábitos no saludables
    psicoactivas = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Sustancias Psicoactivas')
    alcohol = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Alcohol')
    fumador = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Fumador')
    estres = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Estrés')
    sedentarismo = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Sedentarismo')

    # Examen físico
    presion_arterial = fields.Char(string='T.A.')
    frecuencia_cardiaca = fields.Char(string='Frecuencia Cardiaca')
    peso = fields.Char(string='Peso (kg)')

    # Impresión diagnóstica
    analisis_plan = fields.Text(string='Análisis y Plan')
    principal = fields.Selection([ ('si', 'Sí'),('no', 'No'),],string='Principal')
    cod_diag = fields.Char(string='Código Diagnóstico')
    descripcion_diag = fields.Char(string='Descripción Diagnóstico')
    finalidad_diag = fields.Char(string='Finalidad Diagnóstico')

    # Ordenamiento
    codigo_proc = fields.Many2one('medi_serv.trata_proc_cirugia', string='Código Procedimiento')
    nombre_proc = fields.Char(related='codigo_proc.name', string='Nombre Procedimiento')
    cantidad_proc = fields.Integer(string='Cantidad')
    nota_proc = fields.Char(string='Nota')
    tipo_proc = fields.Selection([
        ('laboratorio', 'Laboratorio'),
        ('imagen', 'Imagen'),
        ('otros', 'Otros')
    ], string='Tipo')

    # Medicamento
    codigo_medic = fields.Many2one('medi_serv.medicamento', string='Código Medicamento')
    nombre_medic = fields.Char(related='codigo_medic.nombre', string='Nombre Medicamento')
    dosificacion = fields.Char(string='Dosificación')
    cantidad_medic = fields.Integer(string='Cantidad')
    dias_tratamiento = fields.Integer(string='Días de Tratamiento')
