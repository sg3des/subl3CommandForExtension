import sublime, sublime_plugin, os

class CommandForExtensionCommand(sublime_plugin.TextCommand):
	def run(self, edit, commands = None):
		view = sublime.Window.active_view(sublime.active_window())
		filename, ext = os.path.splitext(view.file_name())

		settings = sublime.load_settings('CommandForExtension.sublime-settings')
		commands = settings.get("commands")

		for item in commands:
			if ext in item["extension"]:
				self.view.window().run_command(item["command"])
				break
			if len(item["extension"]) == 0:
				self.view.window().run_command(item["command"])
