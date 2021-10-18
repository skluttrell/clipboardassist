# -*- coding: UTF-8 -*-

import addonHandler
import globalPluginHandler
import scriptHandler
import ui
from ctypes import windll

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	@scriptHandler.script(
		description="Queries the data on the Windows clipboard",
		gesture="kb:NVDA+shift+z"
	)
	def script_QueryClipboard(self, gesture):
		if windll.user32.OpenClipboard(None):
			if scriptHandler.getLastScriptRepeatCount() == 0:
				if not windll.user32.CountClipboardFormats(): # Clipboard is empty
					#Translators: message to indicate that there is nothing stored on the clipboard.
					ui.message(_("the clipboard is empty"))
				else: # Check clipboard data
					if windll.user32.IsClipboardFormatAvailable(1): # Text
						#Translators: message to indicate that there is text (UTF-8) data currently stored on the clipboard
						ui.message(_("the clipboard contains text"))
					elif windll.user32.IsClipboardFormatAvailable(2): # bitmap
						#Translators: message to indicate that there is image/screenshot (bitmap) data currently stored on the clipboard
						ui.message(_("the clipboard contains image data"))
					elif windll.user32.IsClipboardFormatAvailable(15): # File(s)
						#Translators: message to indicate that there is a file (or files) currently stored on the clipboard
						ui.message(_("the clipboard contains a file"))
					else: # Unknown/anything else
						#Translators: message to indicate that there is data in an unknown format currently stored on the clipboard
						ui.message(_("the clipboard contains unknown data"))
			else: # Gesture pressed again
				windll.user32.EmptyClipboard()
				#Translators: message confirming that the clipboard has been cleared of all data
				ui.message(_("cleared clipboard"))
			windll.user32.CloseClipboard()