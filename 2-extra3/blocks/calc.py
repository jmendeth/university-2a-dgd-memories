# -*- coding: utf-8

top_level = True

ports = [
("OSC_50", "input", ur"Rellotge a \SI{50}{\mega\hertz} intern"),
("KEY[0]", "input", ur"Tecla~0 de la placa (actiu baix)"),
("COL[3..0]", "input", ur"Pins de columna del teclat"),
("ROW[3..0]", "output", ur"Pins de fila del teclat"),
("LED_GREEN[7..0]", "output", ur"LEDs verds de la placa"),
("LED_RED[7..0]", "output", ur"LEDs vermells de la placa"),
("HEX7[6..0]", "output", ur"Display set-segments~7"),
("HEX6[6..0]", "output", ur"Display set-segments~6"),
("HEX5[6..0]", "output", ur"Display set-segments~5"),
("HEX4[6..0]", "output", ur"Display set-segments~4"),
("HEX3[6..0]", "output", ur"Display set-segments~3"),
("HEX2[6..0]", "output", ur"Display set-segments~2"),
("HEX1[6..0]", "output", ur"Display set-segments~1"),
("HEX0[6..0]", "output", ur"Display set-segments~0"),
]

description = ur'''
Disseny a carregar a la placa FPGA.

Implementa una calculadora BCD amb signe, controlada pel teclat connectat a la placa.
Els dos factors es mostren a $HEX7, HEX6$ i $HEX5, HEX4$ respectivament, i el resultat
a $HEX2, HEX1, HEX0$.

El disseny es pot resetejar prement la tecla~0 de la placa.
'''

implementation = ur'''
En primer lloc, es fa servir \textsf{f\_div} per a obtenir un rellotge de més
baixa freqüència, que assignarem a $clk$ i es farà servir en la resta del disseny.
La tecla~0 de la placa es porta a $nrst$ i també es farà servir com a reset del disseny.

Llavors, es fa servir el bloc \textsf{keytest} per a escanejar el teclat i
s'obtenen els senyals $nkey$ i $keycode$. 

Es porta tot al bloc \textsf{ppal} que és on s'efectua tot el treball. Aquest bloc
exposa com a sortides el mode actual en que es troba ($show$), l'operació que està efectuant ($selop$),
els factors ($sigA, opA$ i $sigB, opB$) i el resultat $sigRes, res$.

Els LEDs estan controlats per una instància de \textsf{leds} on portem $show$ i $selop$.
Els displays estan controlats per una instància de \textsf{hex\_disps} on portem el signe i
mòdul dels factors i resultat, a les entrades amb el mateix nom.
'''
