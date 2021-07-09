TOKENS_FILE_NAME = "token.txt"

def get_tokens():
	with open(TOKENS_FILE_NAME, 'r') as tokens:

		input_tokens = []

		for token in tokens:
			input_tokens.append(token.rstrip())

	return input_tokens
