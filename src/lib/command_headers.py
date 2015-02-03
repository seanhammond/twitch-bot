from src.config.config import *

commands = {
	'!test': {
		'limit': 30,
		'return': 'This is a test!'
	},

	'!randomemote': {
		'limit': 0,
		'argc': 0,
		'return': 'command'
	},

	'!jesus': {
		'limit': 0,
		'argc': 0,
		'return': 'John 3:16 - For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life'
	},

	'!plugdj': {
		'limit': 10,
		'argc': 0,
		'return': 'https://plug.dj/sheezle/'
	},

	'!nick': {
		'limit': 0,
		'argc': 0,
		'return': 'Hi, Im Nick and I love Bailey Jay!'
	}
}










for channel in config['channels']:
	for command in commands:
		commands[command][channel] = {}
		commands[command][channel]['last_used'] = 0
