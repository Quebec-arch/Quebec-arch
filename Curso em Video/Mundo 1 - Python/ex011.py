larg = float(input('Lagura da parede: '))
alt = float(input('Altura da parede: '))
ar = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, ar))
tinta = ar / 2
print('Para pintar essa parede você ira precisar de {}L de tinha'.format(tinta))