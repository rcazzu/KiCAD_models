# -*- coding: utf-8 -*-
"""KiCad 10 PCB Action Plugin: ubicar H1-H4 a 4 mm del contorno."""
import pcbnew
import wx

MARGEN_MM = 4.0


class PosicionarTornillos(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Posicionar tornillos (4 mm)"
        self.category = "Herramientas de PCB"
        self.description = "Alinea H1-H4 a 4 mm de las esquinas de Edge.Cuts"
        self.show_toolbar_button = False

    def Run(self):
        board = pcbnew.GetBoard()
        if board is None:
            wx.MessageBox("No hay ninguna PCB abierta.", self.name, wx.OK | wx.ICON_ERROR)
            return

        referencias = ("H1", "H2", "H3", "H4")
        huellas = {ref: board.FindFootprintByReference(ref) for ref in referencias}
        faltantes = [ref for ref, fp in huellas.items() if fp is None]
        if faltantes:
            wx.MessageBox("No encuentro estas huellas: " + ", ".join(faltantes) +
                          "\nNo se movio ningun agujero.", self.name, wx.OK | wx.ICON_ERROR)
            return

        # Requiere un contorno exterior rectangular cerrado en Edge.Cuts.
        try:
            bbox = board.GetBoardEdgesBoundingBox()
            izq, der = bbox.GetLeft(), bbox.GetRight()
            sup, inf = bbox.GetTop(), bbox.GetBottom()
            margen = pcbnew.FromMM(MARGEN_MM)
            if der - izq <= 2 * margen or inf - sup <= 2 * margen:
                raise ValueError("La PCB es demasiado pequena para este margen.")
        except Exception as exc:
            wx.MessageBox("No pude leer los limites de Edge.Cuts:\n" + str(exc),
                          self.name, wx.OK | wx.ICON_ERROR)
            return

        destinos = {
            "H1": (izq + margen, sup + margen),
            "H2": (der - margen, sup + margen),
            "H3": (izq + margen, inf - margen),
            "H4": (der - margen, inf - margen),
        }
        for ref, (x, y) in destinos.items():
            huellas[ref].SetPosition(pcbnew.VECTOR2I(int(x), int(y)))
        pcbnew.Refresh()
        wx.MessageBox("H1-H4 posicionados a 4 mm de los limites de la PCB.\n"
                      "Verifica el contorno, las separaciones y ejecuta el DRC antes de fabricar.",
                      self.name, wx.OK | wx.ICON_INFORMATION)


PosicionarTornillos().register()
