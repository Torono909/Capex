import Capex
while True:
	text = input("Capex > ")
	print(text)
	result, error = Capex.run(text)

if error: print(error.as_string())
else: print(result)
