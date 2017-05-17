#encoding "utf8"

Designation -> Noun<kwtype="указание">;
TimeOfDay -> Noun<kwtype="время_суток">;

DayNum -> AnyWord<wff=/([1-2]?[0-9])|(3[0-1])/> | OrdinalNumeral | Word<gram="NUM">;
Day -> DayNum+;

Month-> Noun<kwtype="месяц">;

YearNum -> OrdinalNumeral | AnyWord<wff=/[1-2]?[0-9]{1,3}/> | Word<gram="NUM">;
YearDescr -> "год" | "г" Punct | "гг" Punct;
Year -> YearNum<gnc-agr[1]>+ YearDescr<gnc-agr[1], rt>;

CenturyDescr -> "век" | "в" Punct | "столетие";
CenturyNum -> AnyWord<wff=/([1-2]?[0-9])|(3[0-1])/> | OrdinalNumeral| Word<gram="NUM">;
Century -> CenturyNum<gnc-agr[1]>+ CenturyDescr<gnc-agr[1], rt>;

MilleniumDescr -> "тысячелетие";
MilleniumNum -> AnyWord<wff=/([1-2]?[0-9])|(3[0-1])/> | OrdinalNumeral | Word<gram="NUM">;
Millenium -> MilleniumNum<gnc-agr[1]>+ MilleniumDescr<gnc-agr[1], rt>;


Date-> Day interp (Date.Day) Month interp (Date.Month)
	| Day interp (Date.Day) Month interp (Date.Month) Year interp (Date.Year)
	| Day interp (Date.Day) Punct Month interp (Date.Month) Punct Year interp (Date.Year) Punct
	| Month interp (Date.Month) Year interp (Date.Year)
	| Year interp (Date.Year)
	| Year interp (Date.Year) Century interp (Date.Century)
	| Century interp (Date.Century)
	| Century interp (Date.Century) Millenium interp (Date.Millenium)
	| Millenium interp (Date.Millenium)
	| TimeOfDay interp (Date.TimeOfDay) Day interp (Date.Day) Month interp (Date.Month)
	| TimeOfDay interp (Date.TimeOfDay) Day interp (Date.Day) Month interp (Date.Month) Year interp (Date.Year)
	| TimeOfDay interp (Date.TimeOfDay) Day interp (Date.Day) Punct Month interp (Date.Month) Punct Year interp (Date.Year) Punct
	| Designation interp (Date.Designation) Month interp (Date.Month) Year interp (Date.Year)
	| Designation interp (Date.Designation) Year interp (Date.Year)
	| Designation interp (Date.Designation) Year interp (Date.Year) Century interp (Date.Century)
	| Designation interp (Date.Designation) Century interp (Date.Century)
	| Designation interp (Date.Designation) Century interp (Date.Century) Millenium interp (Date.Millenium)
	| Designation interp (Date.Designation) Millenium interp (Date.Millenium); 


Event -> Date;