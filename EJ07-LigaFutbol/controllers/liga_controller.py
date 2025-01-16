# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class LigaController(http.Controller):
    @http.route('/eliminarempates', type='http', auth='public', methods=['GET'])
    def eliminar_empates(self):
        """
        Elimina todos los partidos empatados y muestra el número de partidos eliminados.
        """
        # Buscar todos los partidos empatados
        partidos_empatados = request.env['liga.partido'].sudo().search([('goles_casa', '=', 'goles_fuera')])
        # Contar los partidos eliminados
        num_partidos_eliminados = len(partidos_empatados)
        # Eliminar los partidos empatados
        partidos_empatados.unlink()

        # Mostrar el número de partidos eliminados
        return f"<html><body><h1>Partidos eliminados: {num_partidos_eliminados}</h1></body></html>"

