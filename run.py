# -*- coding: utf-8 -*-
"""
    run.py
"""
from gmonki import app

if __name__ == "__main__":
	# Flask debugger by default
	if app.debug: use_debugger = True
	
	# Enable Eclipse / Aptana debugger if indicated
	try: use_debugger = not(app.config.get('DEBUG_WITH_APTANA'))
	except: pass

	#use_debugger, use_reloader only active when debug=True
	app.run(debug=app.debug, use_debugger=use_debugger, use_reloader=use_debugger)
