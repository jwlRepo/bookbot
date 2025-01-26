def main():
	f_src = 'books/frankenstein.txt'
	with open(f_src) as f:
		file_contents=f.read()
	print(f'--- Begin report of {f_src} ---')
	print(f'{count_words(file_contents)} words found in the document\n')
	char_dict = char_cnts(file_contents)
	for k, v in char_dict.items():
		if k.isalpha():
			print(f"The '{k}' character was found {v} times")
	print(f'--- End report ---')

def char_cnts(s):
	data = {}
	for w in s:
		w = w.lower()
		if w in data:
			data[w] += 1
		else:
			data[w] = 1
	return data

def count_words(s):
	w=s.split()
	return len(w)

main()
