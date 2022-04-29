from doctest import script_from_examples
import subprocess, sys
def balls():
	applescript = """
	set input to "im watching u"

	tell application "Messages"
		set targetBuddy to "(###)-###-####"
		set targetService to id of 1st account whose service type = iMessage
		set textMessage to input
		set theBuddy to participant targetBuddy of account id targetService
		send textMessage to theBuddy
	end tell

	"""
	args = [item for x in [("-e",l.strip()) for l in applescript.split('\n') if l.strip() != ''] for item in x]
	proc = subprocess.Popen(["osascript"] + args ,stdout=subprocess.PIPE )
	progname = proc.stdout.read().strip()
	sys.stdout.write(str(progname))
