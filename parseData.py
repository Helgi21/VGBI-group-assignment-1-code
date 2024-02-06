import csv

class ParseData:
	def __init__(self) -> None:
		self.VN_PATH = "./data/visitalaNeysluverds.csv"
		self.FS_PATH = "./data/fjoldi_starfa_samtals.csv"
		self.data = {
			"VN": [],
			"FS": [],
			"VN_header": ["Ársfjórðungur" ,"Vísitala neysluverðs Vísitala", "Vísitala neysluverðs Mánaðarbreyting, %", "Vísitala neysluverðs Ársbreyting, %", "Vísitala neysluverðs Ársbreyting síðasta mánuð, %", "Vísitala neysluverðs Ársbreyting síðustu 3 mánuði, %", "Vísitala neysluverðs Ársbreyting síðustu 6 mánuði, %", "Vísitala neysluverðs án húsnæðis Vísitala;Vísitala neysluverðs án húsnæðis Mánaðarbreyting, %", "Vísitala neysluverðs án húsnæðis Ársbreyting, %", "Vísitala neysluverðs án húsnæðis Ársbreyting síðasta mánuð, %", "Vísitala neysluverðs án húsnæðis Ársbreyting síðustu 3 mánuði, %", "Vísitala neysluverðs án húsnæðis Ársbreyting síðustu 6 mánuði, %"],
			"FS_header": ["Ársfjórðungur", "Mælikvarði", "Starfandi", "A. Landbúnaður, skógrækt og fiskveiðar", "B-E. Framleiðsla, námugröftur, veitustarfsemi og meðhöndlun úrgangs", "C. Framleiðsla", "F. Byggingarstarfsemi og mannvirkjagerð", "G-I. Heildsala og verslun, samgöngur og geymslusvæði, rekstur veitinga- og gististaða","J. Upplýsingar og fjarskipti", "K. Fjármála- og vátryggingastarfsemi", "M-N. Ýmis sérhæfð þjónusta", "O-Q. Opinber stjórnsýsla, fræðslustarfsemi, heilbrigðis- og félagsþjónusta", "R-U. Önnur starfsemi", "Samtals"]
		}

	def parse(self) -> dict:
		self.__read_data()
		self.__fix_data()
		return self.data

	def __read_data(self) -> None:
		with open(self.VN_PATH, newline='', encoding="utf8") as csvfile:
			reader = csv.reader(csvfile, delimiter=';', quotechar='"')
			for row in reader:
				self.data["VN"].append(row)

		with open(self.FS_PATH, newline='', encoding="utf8") as csvfile:
			reader = csv.reader(csvfile, delimiter=';', quotechar='"')
			for row in reader:
				self.data["FS"].append(row)

	def __fix_data(self) -> None:
		# Fix vísitala neysluverðs    
		# Discard data before 1991 and after Q3 2023
		filteredVN = []
		for line in self.data["VN"]:
			if (line[0][:4].isdigit() == True and int(line[0][:4]) >= 1991 and int(line[0][:4]) < 2024):
				filteredVN.append(line)
			elif (line[0][:4].isdigit() == True and int(line[0][:4]) == 2024 and int(line[0][-2:]) > 9):
				filteredVN.append(line)
			
		# Keep only 1st and then every 3rd row
		self.data["VN"] = filteredVN[::3]

		# Rename 1st column of every line
		for line in self.data["VN"]:
			if line[0][-2:] == "01":
				line[0] = line[0][:4] + "Q1"
			elif line[0][-2:] == "04":
				line[0] = line[0][:4] + "Q2"
			elif line[0][-2:] == "07":
				line[0] = line[0][:4] + "Q3"
			elif line[0][-2:] == "10":
				line[0] = line[0][:4] + "Q4"
				

		# Fix fjöldi starfa
		# Remove header
		self.data["FS"].pop(0)
		self.data["FS"].pop(0)
		self.data["FS"].pop(0)

		for index, line in enumerate(self.data["FS"]):
			line.insert(0, index)
			line[1] = line[1].replace("Á", "Q")
			for li in line[4:]:
				# if not number, replace with 0
				if li.isdigit() == False:
					line[line.index(li)] = 0

