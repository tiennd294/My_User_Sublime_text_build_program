import sublime
import sublime_plugin

from json import dumps

class BuildEchoCommand(sublime_plugin.WindowCommand):
	def run(self, **kwargs):
		view = self.window.create_output_panel("Build Echo")

		view.setting().set("line_numbers", False)
		view.setting().set("gutter", False)
		view.setting().set("scroll_past_end", False)

		view.run_command("append", {"characters":dumps(kwargs, indent = 4)})
		self.window.run_command("show_panel", "output.build echo")