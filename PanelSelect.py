import sublime
import sublime_plugin

class PanelSelectCommand(sublime_plugin.WindowCommand):
   """ This plugin allows easy changing of panel focus """

   def __init__(self, window):
      super().__init__(window)

   def run(self, panel=None):
      """ Main run function """
      size = get("panel_size")
      self.layout3 = {'cells': [[0, 0, 1, 1], [1, 0, 2, 1], [2, 0, 3, 1]], 'rows': [0.0, 1.0], 'cols': [0.0, size, size*2, 1.0]}
      self.layout2 = {'cells': [[0, 0, 1, 1], [1, 0, 2, 1], [2, 0, 3, 1]], 'rows': [0.0, 1.0], 'cols': [0.0, size, 1.0-size, 1.0]}
      self.layout1 = {'cells': [[0, 0, 1, 1], [1, 0, 2, 1], [2, 0, 3, 1]], 'rows': [0.0, 1.0], 'cols': [0.0, 1.0-(size*2), 1.0-size, 1.0]}

      debug ("Panel size is: " + str(size))
      if size > 0.5:
         debug ("Panel size is too large, must be less than 0.5")
      
      # select which panel layout to use
      if int(panel) is 3:
         self.window.set_layout(self.layout3)
         self.window.focus_group(2)
      elif int(panel) is 2:
         self.window.set_layout(self.layout2)
         self.window.focus_group(1)
      elif int(panel) is 1:
         self.window.set_layout(self.layout1)
         self.window.focus_group(0)


SETTINGS_FILE = "PanelSelect.sublime-settings"
GLOBAL_PREFERENCES = "Preferences.sublime-settings"
class Settings:
    """ Interface for communicating with settings """
    plugin = None

    def load():
        """Loads the settings for the plugin"""
        Settings.plugin = sublime.load_settings(SETTINGS_FILE)
 
    def get(name):
        """ Gets a value from the plugin settings """
        if not Settings.plugin:
            Settings.load()

        plugin = Settings.plugin
        return plugin.get(name)


def get(name):
    """ Gets a value from settings class """
    return Settings.get(name)

def debug(message):
   """ Print a message to the console """
   if get("debug") is True:
      print (message)
