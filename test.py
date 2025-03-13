from src.texts import Text


company = 'artel'

text = Text(company_name=company, products=['podokonnik', 'stol', 'um'])

txt1 = text.get_text('podokonnik')
txt2 = text.get_text('podokonnik')
txt3 = text.get_text('podokonnik')


print(txt1)
print(txt2)
print(txt3)


