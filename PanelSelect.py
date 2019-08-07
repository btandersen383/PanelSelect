import sublime
import sublime_plugin


class PanelSelectCommand(sublime_plugin.WindowCommand):
   """ This plugin allows easy changing of panel focus """

   current_panel = 1

   layout3 = {'cells': [[0, 0, 1, 1], [1, 0, 2, 1], [2, 0, 3, 1]], 'rows': [0.0, 1.0], 'cols': [0.0, 0.15, 0.30, 1.0]}
   layout2 = {'cells': [[0, 0, 1, 1], [1, 0, 2, 1], [2, 0, 3, 1]], 'rows': [0.0, 1.0], 'cols': [0.0, 0.15, 0.85, 1.0]}
   layout1 = {'cells': [[0, 0, 1, 1], [1, 0, 2, 1], [2, 0, 3, 1]], 'rows': [0.0, 1.0], 'cols': [0.0, 0.7, 0.85, 1.0]}
   def run(self, panel=None):
      if int(panel) is 3:
         self.window.set_layout(self.layout3)
         self.window.focus_group(2)
      elif int(panel) is 2:
         self.window.set_layout(self.layout2)
         self.window.focus_group(1)
      elif int(panel) is 1:
         self.window.set_layout(self.layout1)
         self.window.focus_group(0)
