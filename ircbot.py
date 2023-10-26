import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr

class IRCBot(irc.bot.SingleServerIRCBot):
	def __init__(self, server, port, nickname, channel):
		irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
		self.channel = channel
		self.log_file = open("irc_logs.txt", "a")

	def on_welcome(self, connection, event):
		connection.join(self.channel)

	def on_pubmsg(self, connection, event):
		nickname = event.source.nick
		message = event.arguments[0]
		self.log_file.write(f"[{nickname}] {message}\n")
		self.log_file.flush()

		target = self.channel
		send_msg(connection, target, "Hello from a human :^)")	
		print("message sent")

def send_msg(connection, target, message):
	connection.privmsg(target, message)


def main():
	server = "irc.tdtdt.net"
	port = 6667
	nickname = "caoutchouc"
	channel = "#muzikstation"

	bot = IRCBot(server, port, nickname, channel)
	bot.start()
	print("bot started")

if __name__ == "__main__":
	print("bot running")
	main()
