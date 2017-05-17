#encoding "utf8"

S -> Word<gram="persn"> interp (FIO.Name)
	| 	Word<gram="persn"> interp (FIO.Name) Word<gram="patrn"> interp (FIO.Patron)
	| 	Word<gram="persn"> interp (FIO.Name) Word<gram="patrn"> interp (FIO.Patron) Word<gram="famn"> interp (FIO.Surname)
	| 	Word<gram="persn"> interp (FIO.Name) Word<gram="famn"> interp (FIO.Surname)
	| 	Word<gram="famn"> interp (FIO.Surname)
	| 	Word<gram="persn"> interp (FIO.Name) Word<h-reg1> interp (FIO.Patron)
	| 	Word<gram="persn"> interp (FIO.Name) Word<h-reg1> interp (FIO.Patron) Word<h-reg1>
	| 	Word<gram="famn"> interp (FIO.Surname);