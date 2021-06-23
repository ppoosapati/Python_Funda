#acronyms = ['lol', 'idk', 'tbh']
#translations = ['laugh out loud', 'i dont know', 'to be honest']
#print (acronyms)
#print (translations)

acronyms = { 'lol' : 'laugh out loud', 'idk': 'i dont know', 'tbh' : 'to be honest'}
print(acronyms['lol'] + ", " + acronyms['idk'] + ", " + acronyms['tbh'])
print(acronyms['lol'] + ", " + acronyms['idk'] + " what had happened " + acronyms['tbh'])
# the below print statement gives error since we dont have a key-value pair for stfu
# print(acronyms['stfu'] + ", " + acronyms['idk'] + " what had happened " + acronyms['tbh'])
# print(acronyms.get('stfu') + ", " + acronyms.get('idk') + " what had happened " + acronyms.get('tbh'))
print(acronyms.get('lol'))
print(acronyms.get('stfu'))

del acronyms['lol']
acronyms['stfu'] = 'shut the f up'
print(acronyms.get('stfu'))
print(acronyms.get('stfu') + ", " + acronyms.get('idk') + " what had happened " + acronyms.get('tbh'))
