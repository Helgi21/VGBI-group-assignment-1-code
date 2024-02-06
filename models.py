from sqlalchemy import Table, Column, Float, String, Integer, MetaData

metadata_obj = MetaData()

VN_table = Table(
	"VN",
	metadata_obj,
	Column("Ársfjórðungur", String(7), primary_key=True),
	Column("Vísitala neysluverðs Vísitala", Float),
	Column("Vísitala neysluverðs Mánaðarbreyting, %", Float),
	Column("Vísitala neysluverðs Ársbreyting, %", Float),
	Column("Vísitala neysluverðs Ársbreyting síðasta mánuð, %", Float),
	Column("Vísitala neysluverðs Ársbreyting síðustu 3 mánuði, %",Float),
	Column("Vísitala neysluverðs Ársbreyting síðustu 6 mánuði, %",Float),
	Column("Vísitala neysluverðs án húsnæðis Vísitala;Vísitala neysluverðs án húsnæðis Mánaðarbreyting, %",Float),
	Column("Vísitala neysluverðs án húsnæðis Ársbreyting, %",Float),
	Column("Vísitala neysluverðs án húsnæðis Ársbreyting síðasta mánuð", Float),
	Column("Vísitala neysluverðs án húsnæðis Ársbreyting síðustu 3 mánuði, %",Float),
	Column("Vísitala neysluverðs án húsnæðis Ársbreyting síðustu 6 mánuði, %", Float)
)

FS_table = Table(
	"FS",
	metadata_obj,
	Column("Id", Integer, primary_key=True, autoincrement=True),
	Column("Ársfjórðungur", String(7)),
	Column("Mælikvarði", String),
	Column("Starfandi", String),
	Column("A. Landbúnaður, skógrækt og fiskveiðar", Integer),
	Column("B-E. Framleiðsla, námugröftur, veitustarfsemi og meðhöndlun úrgangs", Integer),
	Column("C. Framleiðsla", Integer),
	Column("F. Byggingarstarfsemi og mannvirkjagerð", Integer),
	Column("G-I. Heildsala og verslun, samgöngur og geymslusvæði, rekstur veitinga- og gististaða",Integer),
	Column("J. Upplýsingar og fjarskipti", Integer),
	Column("K. Fjármála- og vátryggingastarfsemi", Integer),
	Column("M-N. Ýmis sérhæfð þjónusta", Integer),
	Column("O-Q. Opinber stjórnsýsla, fræðslustarfsemi, heilbrigðis- og félagsþjónusta", Integer),
	Column("R-U. Önnur starfsemi", Integer),
	Column("Samtals",Integer),
)
