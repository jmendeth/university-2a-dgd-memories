# -*- coding: utf-8

ports = [
("comp[2..0]", "input", ur"Sortida per als indicadors de l'estat del joc"),
("LED_GREEN[7..0]", "output", ur"LEDs verds de la placa"),
]

description = ur'''
Encen els LEDs de la placa en un patró especificat per representar
l'estat de joc de $comp$.

Vegeu la subsecció~\ref{sub:3-control}
(pàgina~\pageref{sub:3-control}) per a una llista dels
possibles valors de $comp$ i els seus significats.
'''

unspecs = ur'''
La sortida no està definida si $comp$ no representa cap estat de joc conegut.
'''

implementation = ur'''
Implementat mitjançant la taula de veritat.
'''

simulation = ur'''
Comprovem que el patró de LEDs correspon amb l'entrada en tot moment.
'''
