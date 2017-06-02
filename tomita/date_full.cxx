#encoding "utf8"

Designation -> Noun<kwtype="указание">;
TimeOfDay -> Noun<kwtype="время_суток">;

DayNum -> AnyWord<wff=/([1-2]?[0-9])|(3[0-1])/> | OrdinalNumeral | Word<gram="NUM">;
Day -> DayNum+;

BCDescr -> "до н.э." | "до нашей эры";

Month-> Noun<kwtype="месяц">;

// YearWord -> OrdinalNumeral<gnc-agr[1]> YearDescr<gnc-agr[1]>
//    | Word<gram="NUM", gnc-agr[1]> YearDescr<gnc-agr[1]>;
YearNum -> AnyWord<wff=/[1-2]?[0-9]{1,3}/>;
YearDef -> "год" | "г" Punct | "гг" Punct;
YearDescr -> YearDef (BCDescr interp (Date.IsBC));

// CenturyDescr -> "век" | "в" Punct | "столетие";
// CenturyNum -> AnyWord<wff=/([1-2]?[0-9])|(3[0-1])/> | OrdinalNumeral| Word<gram="NUM">;
// Century -> CenturyNum<gnc-agr[1]>+ CenturyDescr<gnc-agr[1], rt>  (BCDescr interp (Date.IsBC));

// MilleniumDescr -> "тысячелетие";
// MilleniumNum -> AnyWord<wff=/([1-2]?[0-9])|(3[0-1])/> | OrdinalNumeral | Word<gram="NUM">;
// Millenium -> MilleniumNum<gnc-agr[1]>+ MilleniumDescr<gnc-agr[1], rt>;


Date-> (Day interp (Date.Day)) Month interp (Date.Month) YearNum interp (Date.Year) (YearDescr)
	| Month interp (Date.Month) YearNum interp (Date.Year) (YearDescr)
	| YearNum interp (Date.Year) YearDescr;
//	| YearWord interp (Date.Year);


//	| Designation interp (Date.Designation) Month interp (Date.Month) Year interp (Date.Year)
//	| Designation interp (Date.Designation) Year interp (Date.Year);
// 	| Century interp (Date.Century)
// 	| Century interp (Date.Century) Millenium interp (Date.Millenium)
// 	| Millenium interp (Date.Millenium)
// 	| Designation interp (Date.Designation) Year interp (Date.Year) Century interp (Date.Century)
// 	| Designation interp (Date.Designation) Century interp (Date.Century)
// 	| Designation interp (Date.Designation) Century interp (Date.Century) Millenium interp (Date.Millenium)
// 	| Designation interp (Date.Designation) Millenium interp (Date.Millenium);

HyphenDescr -> Hyphen | '-';

DateInterval -> (Day interp (Date.Day)) Month interp (Date.Month) YearNum interp (Date.Year) HyphenDescr interp (Date.IsInterval)
		(Day interp (Date.Day)) Month interp (Date.Month) YearNum interp (Date.Year)
	| (Day interp (Date.Day)) Month interp (Date.Month) HyphenDescr interp (Date.IsInterval)
		(Day interp (Date.Day)) Month interp (Date.Month) YearNum interp (Date.Year)
	| Day interp (Date.Day) HyphenDescr interp (Date.IsInterval) Day interp (Date.Day) Month interp (Date.Month) YearNum interp (Date.Year)
	| YearNum interp (Date.Year) HyphenDescr interp (Date.IsInterval) YearNum interp (Date.Year)

	| "с" (Day interp (Date.Day)) Month interp (Date.Month) YearNum interp (Date.Year) "по" interp (Date.IsInterval)
		(Day interp (Date.Day)) Month interp (Date.Month) YearNum interp (Date.Year)
	| "с" (Day interp (Date.Day)) Month interp (Date.Month) "по" interp (Date.IsInterval)
		(Day interp (Date.Day)) Month interp (Date.Month) YearNum interp (Date.Year)
	| "с" Day interp (Date.Day) "по" interp (Date.IsInterval) Day interp (Date.Day) Month interp (Date.Month) YearNum interp (Date.Year)
	| "с" YearNum interp (Date.Year) "по" interp (Date.IsInterval) YearNum interp (Date.Year);

Event -> Date | DateInterval;