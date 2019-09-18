from tkinter import *																								#1
#-----------Frames-----------
raiz = Tk()																											#2
raiz.title("Wirtschaft")																							#3
cuerpo = Frame(raiz)																								#4
cuerpo.pack()																										#5
#---------Variables----------
cantidad = IntVar()																									#6
impuesto = IntVar()																									#7
años = IntVar()																										#8
visualizacion = IntVar()																							#9
borrar = 0																											#10
select = IntVar()																									#11
L_0 = StringVar()																									#12
#-----------Label / Entry----
L_cantidad = Label(cuerpo, text = "      Fälligkeit Darlehen: ").grid(row=1, column=1, sticky=E)					#13
T_cantidad = Entry(cuerpo, textvariable=cantidad).grid(row=1, column=2, sticky=W)									#14
L_u1 = Label(cuerpo, text= "€").grid(row=1, column=3, sticky=W)														#15
L_impuesto = Label(cuerpo, text = "  Ratenkredit: ").grid(row=2, column=1, sticky=E)								#16
T_impuesto = Entry(cuerpo, textvariable=impuesto).grid(row=2, column=2, sticky=W)									#17
L_u2 = Label(cuerpo, text= "%").grid(row=2, column=3, sticky=W)														#18
L_años = Label(cuerpo, text = "         Annuitätendarlehen: ").grid(row=3, column=1, sticky=E)						#19
T_años = Entry(cuerpo, textvariable=años).grid(row=3, column=2, sticky=W)											#20
L_u3 = Label(cuerpo, text= "Años").grid(row=3, column=3, sticky=W)													#21
#-----------Funciones--------
def calcular():																										#22
	global borrar																									#23
	fila = años.get()																								#24
	if borrar != 0:																									#25
		borrar_tabla(borrar)																						#26
		print("Löschen")																							#27
	borrar = fila																									#28
	tabla()																											#29

def resultados(f,repe):																								#30
	global sumat 																									#31
	global imp 																										#32
	global amort 																									#33
	global rent 																									#34
	global q 																										#35
	global n																										#36
	global k																										#37
	global a 																										#38
	n = int(años.get())																								#39
	if repe == 0:																									#40
		imp = int(impuesto.get())																					#41
		sumat = cantidad.get()																						#42
		k = sumat																									#43
		q = 1+imp/100																								#44
		amort = 0																									#45
		rent = (k*q)-k																								#46
	if select.get() == 1:		#pago unico a final del año 														#47
		if f+1 == n:																								#48
			sumat = k																								#49
			imp = (k*q)-k																							#50
			amort = amort + k																						#51
			rent = imp + amort																						#52
		elif f < n:																									#53
			imp = (k*q)-k																							#54
			amort = amort																							#55
			rent = imp																								#56
		repe += 1																									#57
	elif select.get() == 2:		#pago escalable por año 															#58
		if impuesto.get() or cantidad.get() or años.get()!=0:
			if f == 0:																								#59
				sumat = k																							#60
				imp = (k*q)-k																						#61
				amort = k / n																						#62
				rent = amort + imp																					#63
			else:																									#64
				sumat = sumat - amort																				#65
				imp = sumat * (q-1)																					#66
				rent = imp + amort																					#67
			repe += 1																								#68
	elif select.get() == 3:		#pago sin variacion por año 														#69
		if impuesto.get() or cantidad.get() or años.get()!=0:
			if f == 0:																								#70
				sumat = k																							#71
				imp = sumat * (q-1)																					#72
				amort = (k*(q**n)*(q-1))/((q**n)-1) - imp															#73
				rent = (k*(q**n)*(q-1))/((q**n)-1)																	#74
			else:																									#75
				amort = rent - imp																					#76
				sumat = sumat - amort																				#77
				imp = sumat * (q-1)																					#78
				amort = rent - imp																					#79
				rent = rent																							#80
			repe += 1																								#81
# Sumatorio | Impuesto | Amortizacion | Renta
def tabla():																										#82
	global sumat																									#83
	global imp																										#84
	global amort																									#85
	global rent																										#86
	sumat = ''																										#87
	imp = ''																										#88
	amort = ''																										#89
	rent = ''																										#90
	L_Sumatorio = Label(cuerpo, text="| Darlehens- \n restschuld ").grid(row=0, column=6)							#91
	L_impuesto = Label(cuerpo, text="|  Zinsen  |").grid(row=0, column=7)											#92
	L_Amortizacion = Label(cuerpo, text="     Tilgung |").grid(row=0, column=8)										#93
	L_Renta = Label(cuerpo, text="  Annuität   |").grid(row=0, column=9)											#94
	print("tabla ejecutandose")																						#95
#---Bucle de visualizacion---																						#96
	for i in range (años.get() + 1):																				#97
		visu(i)																										#98
#---Borrar tabla-------------
def borrar_tabla(a):																								#99
	x = 6																											#100
	for i in range (a+4):																							#101
		for x in range (5,10):																						#102
			L_v = Label(cuerpo, text='                    ').grid(row=i, column=x, sticky=E)						#103
	fila = 0																										#104
	borrar = fila																									#105
#def visu(fila, sumat, imp, amort, rent):
def visu(fila): 																									#106
	global sumat 																									#107
	global imp 																										#108
	global amort																									#109
	global rent 																									#110
	s = str(sumat)																									#111
	i = str(imp)																									#113
	a = str(amort)																									#113
	r = str(rent)																									#114
	if s.count(".") == True:																						#115
		s = (s[0:(len(s))-(((len(s))-(s.rfind("."))))+4])															#116
	if i.count(".") == True:																						#117
		i = (i[0:(len(i))-(((len(i))-(i.rfind("."))))+4])															#118
	if a.count(".") == True:																						#119
		a = (a[0:(len(a))-(((len(a))-(a.rfind("."))))+4])															#120
	if r.count(".") == True:																						#121
		r = (r[0:(len(r))-(((len(r))-(r.rfind("."))))+4])															#122
	L_v = Label(cuerpo, text=s).grid(row=fila, column=6, sticky=E)													#123
	L_v = Label(cuerpo, text=i).grid(row=fila, column=7, sticky=E) 													#124
	L_v = Label(cuerpo, text=a).grid(row=fila, column=8, sticky=E) 													#125
	L_v = Label(cuerpo, text=r).grid(row=fila, column=9, sticky=E)													#126
	resultados(fila,fila) 																							#127
	if select.get() != 0: 																							#128
		total(fila, float(imp), float(amort), float(rent)) 															#129
		fila += 1																									#130

def total(f,i,a,r): 																								#131
	global imp  																									#132
	global amort																									#133
	global rent																										#134
	global s_imp																									#135
	global s_amort																									#136
	global s_rent																									#137
	if f == 0:																										#138
		s_imp = float(imp)																							#139
		s_amort = float(amort)																						#140
		s_rent = float(rent)																						#141
		ff=0																										#142
	elif f < n:																										#143
		s_imp = i + s_imp 																							#144
		s_amort = a + s_amort 																						#145
		s_rent =r + s_rent
	if f == n:																										#146
		ff = f+1																									#147
		if str(s_imp).count(".") == True:																			#148
			s_imp = (str(s_imp)[0:(len(str(s_imp)))-(((len(str(s_imp)))-(str(s_imp).rfind("."))))+4])				#149
		if str(s_amort).count(".") == True:																			#150
			s_amort = (str(s_amort)[0:(len(str(s_amort)))-(((len(str(s_amort)))-(str(s_amort).rfind("."))))+4])		#151
		if str(s_rent).count(".") == True:																			#152
			s_rent = (str(s_rent)[0:(len(str(s_rent)))-(((len(str(s_rent)))-(str(s_rent).rfind("."))))+4])			#153
																													#154
		L_v = Label(cuerpo, text="Summe:").grid(row=ff, column=5, sticky=E)											#155
		L_v = Label(cuerpo, text=s_imp).grid(row=ff, column=7, sticky=E)											#156
		L_v = Label(cuerpo, text=s_amort).grid(row=ff, column=8, sticky=E)											#157
		L_v = Label(cuerpo, text=s_rent).grid(row=ff, column=9, sticky=E)											#158
#impuesto = Label(cuerpo)
def accion():																										#159
	if select.get() == 1:																							#160
		opcion.config(text="einmalige Zahlung am Ende des Jahres")													#161
		opcion.grid(row=5, column=1)																				#162
		opc=1																										#163
	elif select.get() == 2:																							#164
		opcion.config(text="        skalierbare Zahlung pro Jahr")													#165
		opcion.grid(row=5, column=1)																				#166
		opc=2																										#167
	elif select.get() == 3:																							#168
		opcion.config(text="       unveränderte Zahlung pro Jahr")													#169
		opcion.grid(row=5, column=1)																				#170
		opc=3																										#171
#-----------Botones----------
Boton = Button(cuerpo, text="Calcular", width=6, command=calcular)													#172
Boton.grid(row=6, column=1)																							#173
#cantidad = Label(cuerpo)
Radiobutton(cuerpo, text="Wahl 1", value=1, variable=select, command=accion).grid( row=4, column=2, sticky =W)		#174
Radiobutton(cuerpo, text="Wahl 2", value=2, variable=select, command=accion).grid( row=5, column=2, sticky =W)		#175
Radiobutton(cuerpo, text="Wahl 3", value=3, variable=select, command=accion).grid( row=6, column=2, sticky =W)		#176
#visualizacion = Label(cuerpo)
if select.get() != 0:																								#177
	L_0.set("")																										#178
	opc=0																											#179
	L_0 = Label(cuerpo, text="   ").grid(row=0, column=0)
else:																												#180
	L_0 = Label(cuerpo, text="Wählen Sie ein Kästchen")																#181
	L_0.grid(row=5, column=1)																						#182
#----------------------------
opcion = Label(cuerpo)																								#183
cuerpo.mainloop()																									#184
raiz.mainloop()																										#185