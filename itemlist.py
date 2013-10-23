item_names = {'498': 'Dual Plasma Cannon', '496': 'Boxing Gloves', '497': 'Plated Boxing Gloves', \
              '24': 'Plasma Pistol', '25': 'Grenade (Frag)', '26': 'Grenade (Plasma)', '27': 'Grenade (Pulse)',\
              '20': 'Crowbar', '21': 'Brass Knuckles', '22': '14mm Pistol', '23': 'Assault Rifle',\
              '28': 'Gatling Laser', '94': 'Shotgun', '407': 'Mega Power Fist', \
	      '406': 'Plasma Pistol (Ext. Cap.)',\
              '405': 'Assault Rifle (Exp. Mag.)', '404': 'Desert Eagle (Exp. Mag.)',\
              '403': 'FN FAL (Night Sight)',\
              '402': 'Magneto-Laser Pistol', '401': 'Laser Rifle (Ext. Cap.)', '400': 'Improved Flamer', \
              '8': '10mm Pistol', '283': 'Tommy Gun', '287': 'Scoped Hunting Rifle', \
              '522': 'Wakizashi Blade ', '10': 'Hunting Rifle', '120': 'Alien Blaster', '122': '9mm Mauser', \
              '268': 'H&K CAWS', '531': 'End Boss Plasma Gun ', '530': 'End Boss Knife ', '371': 'Claw', \
              '372': 'Claw', '292': 'Boxing Gloves','293': 'Plated Boxing Gloves','290': 'Robo Melee Weapon 1', \
              '291': 'Robo Melee Weapon 2', '319': 'Switchblade', '313': '.44 Magnum Revolver', \
              '270': 'Robo Rocket Launcher', '392': 'M72 Gauss Rifle', '391': 'H&K G11E', '116': 'Ripper', \
              '397': 'YK42B Pulse Rifle', '396': 'YK32 Pulse Pistol', '395': 'Vindicator Minigun', \
              '394': 'PPK12 Gauss Pistol', '399': 'Super Cattle Prod', '398': '.44 Magnum (Speed Load)', \
              '118': 'Laser Rifle', '520': 'Heavy Dual Minigun', '7': 'Spear', '421': 'Holy Hand Grenade', \
              '423': 'Gold Nugget', '365': 'Plant Spike', '427': 'Flame Breath', '426': 'Uranium Ore',\
              '300': 'Zip Gun', '299': 'Pipe Rifle', '296': 'HK P90c', '383': 'Shiv', '384': 'Wrench', \
              '385': 'Sawed-Off Shotgun', '386': 'Louisville Slugger', '387': 'M60', '388': 'Needler Pistol', \
              '389': 'Avenger Minigun', '518': 'Dual Minigun', '241': '.223 Pistol', '393': 'Phazer', \
              '517': '"Little Jesus"', '242': 'Combat Shotgun', '332': 'M3A1 "Grease Gun" SMG',\
              '6': 'Sledgehammer', '500': 'FN FAL HPFA', '4': 'Knife', '280': 'Sharpened Spear', \
              '160': 'Cattle Prod', '161': 'Red Ryder BB Gun', '162': 'Red Ryder LE BB Gun', '11': 'Flamer',\
              '115': 'Super Sledge', '13': 'Rocket Launcher', '12': 'minigun', '15': 'Plasma Rifle',\
              '16': 'Laser Pistol', '19': 'Rock', '18': 'Desert Eagle .44', '390': 'Solar Scorcher', \
              '159': 'Molotov Cocktail', '234': 'Spiked Knuckles', '235': 'Power Fist', '236': 'Combat Knife', \
              '233': 'Turbo Plasma Rifle', '45': 'Throwing Knife', '320': 'Sharpened Pole', '5': 'Club', \
              '9': '10mm SMG', '205': 'Flare', '143': 'Sniper Rifle', '489': 'Special Boxer Weapon', \
              '486': 'Refined Uranium Ore', '79': 'Flare', '261': "Jonny's BB Gun", \
              '355': 'Light Support Weapon', '354': 'Pancor Jackhammer', '353': 'XL70E3', '352': 'H&K G11', \
              '351': 'FN FAL', '350': 'Bozar', '334': 'Poison', '311': 'Roentgen Rum','310': 'Gamma Gulp Beer', \
              '273': 'Healing Powder', '110': 'Psycho', '81': 'Iguana-on-a-stick', '87': 'Buffout', \
              '48': 'RadAway', '49': 'Antidote', '40': 'Stimpak', '525': 'Hypo ', '424': 'Monument Chunk', \
              '144': 'Super Stimpak', '473': 'Mutated Toe', '469': 'Rot Gut\n', '109': 'Rad-X', '124': 'Beer', \
              '125': 'Booze', '71': 'Fruit', '103': 'Iguana-on-a-stick', '106': 'Nuka-Cola', \
              '482': 'Bonus +1 Strength ', '481': 'Bonus +1 Intelligence ', '480': 'Bonus +1 Agility', \
              '259': 'Jet','53': 'Mentats','378': 'Cookie','260': 'Jet Antidote','524': "Bridgekeeper's Robes", \
              '74': 'Leather Jacket', '113': 'Robes', '17': 'Combat Armor', '380': 'Metal Armor Mark II ', \
              '379': 'Leather Armor Mark II', '381': 'Combat Armor Mark II', '3': 'Power Armor', \
              '2': 'Metal Armor','239': 'Brotherhood Armor','265': 'Combat Leather Jacket','1': 'Leather Armor',\
              '348': 'Advanced Power Armor', '349': 'Adv. Power Armor MKII', '232': 'Hardened Power Armor', \
              '240': 'Tesla Armor','111': '.44 magnum FMJ','29': '10mm JHP', '362': 'HN AP Needler Cartridge ', \
              '363': '7.62mm ', '360': '9mm', '361': 'HN Needler Cartridge', '121': '9mm ball', \
              '382': 'Flamethrower Fuel MKII ', '95': '12 ga. Shotgun Shells', '163': "BB's", \
              '39': 'Micro Fusion Cell', '38': 'Small Energy Cell', '14': 'Explosive Rocket', '33': '14mm AP',\
              '32': 'Flamethrower Fuel', '31': '.44 Magnum JHP', '30': '10mm AP', '37': 'Rocket AP', \
              '36': '5mm AP', '35': '5mm JHP','34': '.223 FMJ','357': '.45 Caliber', '274': 'Robo Rocket Ammo', \
              '359': '4.7mm Caseless', '358': '2mm EC','216': "Maxon's History", '217': "Maxson's Journal", \
              '215': 'Brotherhood History', '212': 'Tandi (do not use)', '210': 'Stealth Boy (on)', \
              '127': 'Rope', '218': 'Light Healing (do not use)', '219': 'Medium Healing (do not use)', \
              '227': 'Small Dusty Box of Some Sort', '499': 'PIPBoy Lingual Enhancer', '494': 'Kokoweef Script',\
              '495': 'Presidential Access Key', '490': 'NCR History Holodisk', '491': 'Mr. Nixon Doll',\
              '492': 'Tanker Fob','493': 'Teachings Holodisk','86': 'Scout Handbook', '224': 'Small Statuette', \
              '23': 'Survey Map ', '450': 'Torn Paper 1', '289': 'Shovel', '288': 'Car Fuel Cell (do not use)', \
              '340': "Doctor's Papers",'341': 'Presidential Pass','342': "Ranger's Pin", '343': "Ranger's Map", \
              '281': "Dixon's Eye", '282': "Clifton's Eye", '285': 'Radscorpion Limbs', '284': 'Meat Jerky', \
              '409': "Paramedic's Bag", '286': 'Firewood', '453': 'Password Paper', '440': 'Bio-Med Gel', \
              '331': "Cat's Paw Issue 5",'263': 'Slag Message','262': 'Rubber Boots','123': 'Psychic Nullifier',\
              '267': "Vic's Water Flask", '266': "Vic's Radio", '126': 'Water Flask', \
              '264': "Smith's Cool Item (do not use)", '269': 'Robot Parts', '91': "Doctor's Bag", \
              '59': 'Motion Sensor', '58': 'Tape', '55': 'Water Chip', '54': 'Stealth Boy', '57': 'Bug', \
              '56': 'Dog Tags', '51': 'Dynamite', '50': 'Reserved (do not use)', '52': 'Geiger Counter', \
              '414': 'Vault 15 Shack Key', '415': 'Spectacles','416': 'Empty Jet Canister','417': 'Oxygen Tank',\
              '410': 'Expanded Lockpick Set', '411': 'Electronic Lockpick MKII', '412': 'Oil Can', \
              '413': 'Stables ID Badge', '297': 'Metal Pole', '373': 'Vault 15 Keycard', '295': 'Cheezy Poofs', \
              '418': 'Poison Tank', '419': 'Mine Parts', '377': 'Vault 15 Computer Parts', \
              '318': 'Empty Hypodermic Needle', '195': 'Brotherhood Honor Code','312': 'Part Requesition Form', \
              '196': 'Mutant Transmission', '191': 'Security Disk', '190': 'FEV Disk', \
              '315': 'Condom (green package)', '192': 'Alpha Experiment Disk', '271': 'Broc Flower', \
	      '117': 'Flower', '89': 'Motor', '275': 'Trophy of Recognition', '276': 'Gecko Pelt', \
              '112': 'Urn', '278': 'Flint', '279': 'Neural Interface', '80': 'First Aid Book',\
              '119': 'Knecklace', '444': "Raider's Map", '84': 'Lockpicks', '85': 'Plastic Explosives',\
	      '305': 'Yellow Reactor Keycard', '140': 'Access Card', '337': 'Lynette Holodisk',\
              '206': 'Dynamite (ticking)', '429': 'Gold Tooth', '428': 'Medical Supplies',\
              '447': "Bishop's Holodisk", '301': 'Clipboard', '366': 'GECK', '420': 'Morningstar Script', \
              '364': 'Robot Motivator', '422': 'Excavator Chip', '441': "Blondie's Dog-Tags", \
              '308': 'Super Tool Kit', '309': 'Talisman', '449': '<unused>', '448': 'Account Book', \
              '298': 'Trapper Town Key', '443': "Tuco's Dog-Tags", '442': "Angel Eyes' Dog-Tags", \
              '302': 'Gecko Holodisk', '303': 'Reactor Holodisk', '304': 'Deck of "Tragic Cards"', \
              '446': 'Vertibird Plans', '306': 'Red Reactor Keycard', '307': '3 Step Plasma Transformer', \
              '445': "Sheriff's Badge", '102': '"Guns and Bullets"', '100': 'Radio', '101': 'Lighter', \
              '294': 'Vault 13 Holodisk', '104': 'Tape Recorder', '519': 'Bottle Caps ', '439': 'Pocket Lint', \
              '436': 'Deck of Cards', '437': 'Deck of Marked Cards', '432': 'Ramirez Box (open)', \
              '433': 'Mirrored Shades', '430': 'Howitzer Shell', '431': 'Ramirez Box (closed)', \
              '458': 'Military Base Holodisk 5', '459': 'Military Base Holodisk 1', '339': 'NCR Spy Holodisk', \
              '338': 'Westin Holodisk', '335': "Moore's Briefcase",'451': 'Torn Paper 2', '452': 'Torn Paper 3',\
              '336': "Moore's Briefcase", '454': 'Explosive switch', '333': 'Heart Pills', \
              '457': "Hubologists' Field Report", '258': 'Hydroelectric Part', '252': "Anna's Gold Locket", \
              '253': 'Fuel Cell Controller', '251': "Anna's Bones", '256': 'False Citizenship Papers', \
              '257': "Cornelius' Gold Watch", '254': 'Fuel Cell Regulator', '255': 'Day Pass', \
              '272': 'Xander Root', '316': 'Condom (red package)', '508': 'Rubber Doll', \
              '509': 'Damaged Rubber Doll', '506': 'Yellow Memory Module', '507': 'Decomposing Body', \
              '504': 'Green Memory Module', '505': 'Red Memory Module', '503': 'Blue Memory Module', \
              '468': "Smitty's Meal",'465': 'Medical Holodisk','317': 'Cosmetics Case', '466': 'Password Paper',\
              '461': 'Military Base Holodisk 3','460': 'Military Base Holodisk 2','463': 'Evacuation Holodisk',\
              '462': 'Military Base Holodisk 4','99': 'Gold Locket','98': 'Junk','193': 'Delta Experiment Disk',\
              '229': 'Small Piece of Machinery', '228': 'Technical Manual', '164': 'Brotherhood Tape', \
              '226': 'Box of Noodles','225': "Cat's Paw Magazine",'92': 'Scorpion Tail', '222': 'Field Switch', \
              '221': 'Security Card', '220': 'Heavy Healing (do not use)', '114': "Tangler's Hand", \
              '314': 'Condom (blue package)', '88': 'Watch', '408': 'Field Medic First Aid Kit', \
              '464': 'Experiment Holodisk', '150': 'Bookshelf (do not use)', '154': 'Shelves (do not use)', \
              '156': 'Shelves (do not use)', '277': 'Golden Gecko Pelt', '238': 'Regulator Transmission', \
              '237': 'Chemistry Journals', '230': 'Vault Records', '231': 'Military Base Security Codes', \
              '47': 'First Aid Kit', '41': 'Money', '322': 'Human Brain', '323': 'Chimpanzee Brain', \
              '321': 'Cybernetic Brain', '326': 'Loaded Dice', '327': 'Easter Egg', '324': 'Abnormal Brain', \
              '325': 'Dice', '328': 'Magic 8 Ball', '329': 'Mutagenic Serum', '142': 'COC Badge', \
              '207': 'Geiger Counter (on)', '141': 'COC Badge', '209': 'Plastic Explosives (ticking)', \
              '208': 'Motion Sensor (on)', '148': 'Bookshelf (do not use)', '77': 'Electronic Lockpick', \
              '76': 'Deans Electronics', '75': 'Tool', '73': 'Big Book of Science', '72': 'Briefcase', \
              '488': 'K-9 Motivator','487': 'Note From Francis','485': "Masticator's Ear",'484': "Player's Ear",\
              '483': 'Fallout 2 Hintbook', '78': 'Fuzzy Painting', '194': "Vree's Experiment Disk",\
 	      '479': 'NavCom Parts', '472': "Hubologists' Holodisk", '356': 'Voice Recognition Module',\
	      '470': 'Ball Gag','471': '"The Lavender Flower"', '476': "Enlightened One's Letter",\
              '477': 'Broadcast Holodisk', '474': 'Daisies', '475': '<unused>',\
              '478': 'Sierra Mission Holodisk','516': 'PIPBoy Medical Enhancer','46': 'bag' , \
              '90': 'Backpack' , '93': 'Bag'}

skills = {0x00: "small guns",0x01: "big guns",0x02: "energy weapons",0x03: "unarmed",\
	  0x04: "melee weapons", 0x05: "throwing", 0x06: "first aid",0x07: "doctor",\
	  0x08: "sneak",0x09: "lockpick",0x0A: "steal",0x0B: "traps", 0x0C: "science",\
	  0x0D: "repair", 0x0E: "speech", 0x0F: "barter", 0x10: "gambling",0x11: "outdoorsman"}

victim_classes = ['men','women','children','supermutants','ghouls','brahmin','radscorpion','rats',\
                  'floaters', 'centaurs', 'robots', 'dogs', 'manti', 'deathclaws', 'plants', 'geckos'\
                  'aliens','giantants','bigbadboss']

# a list of item ids which are weapons
weapon_list = [9,12,11,7,18,21,24,27,79,116,122,160,205,235,242,270,287,292,299,319,\
               350,353,365,383,386,389,392,395,398,401,404,407,426,489,498,518,530,8,\
               13,10,15,19,22,25,28,94,118,143,161,233,236,280,290,293,300,320,351,354,\
               371,384,387,390,393,396,399,402,405,421,427,496,500,520,531,6,5,4,16,20,\
               23,26,45,115,120,159,162,234,241,268,283,291,296,313,332,352,355,372,385,\
               388,391,394,397,400,403,406,423,486,497,517,522]

# a list of item ids which are drugs
drug_list = [334,311,310,273,110,81,87,48,49,40,525,424,144,473,469,109,124,125,71,103,\
             106,482,481,480,53,378,260]

# a list of item ids which are armor
armor_list = [524,74,113,17,380,379,381,3,2,239,265,1,348,349,232,240]

# a list of item ids which are containers
container_list = [93,107,46]

# A dict of perks
perks = { 0x00: "Awareness", 0x01: "Bonus HtH Attacks",0x02: "Bonus HtH Damage",0x03: "Bonus Move",\
          0x04: "Bonus Ranged Damage",0x05: "Bonus Rate of Fire",0x06: "Earlier Sequence",\
          0x07: "Faster Healing",0x08: "More Criticals",0x09: "Night Vision",0x0A: "Presence",\
          0x0B: "Rad Resistance",0x0C: "Toughness",0x0D: "Strong Back",0x0E: "Sharpshooter",\
          0x0F: "Silent Running",0x10: "Survivalist",0x11: "Master Trader",0x12: "Educated",\
          0x13: "Healer",0x14: "Fortune Finder",0x15: "Better Criticals",0x16: "Empathy", 0x17: "Slayer",\
          0x18: "Sniper",0x19: "Silent Death",0x1A: "Action Boy",0x1B: "Mental Block (FO1 only)",\
          0x1C: "Lifegiver",0x1D: "Dodger",0x1E: "Snakeeater",0x1F: "Mr. Fixit",0x20: "Medic",\
          0x21: "Master Thief",0x22: "Speaker",0x23: "Heave Ho!",\
          0x24: "Unimplemented, DO NOT USE! (Friendly Foe in FO1)", 0x25: "Pickpocket", 0x26: "Ghost",\
          0x27: "Cult of Personality",0x28: "Scrounger (FO1 only)",0x29: "Explorer",\
          0x2A: "Flower Child (FO1 only)",0x2B: "Pathfinder",0x2C: "Animal Friend (FO1 only)",\
          0x2D: "Scout",0x2E: "Mysterious Stranger",0x2F: "Ranger",0x30: "Quick Pockets",\
          0x31: "Smooth Talker",0x32: "Swift Learner",0x33: "Tag!",0x34: "Mutate!",\
          0x35: "Nuka-Cola Addiction",0x36: "Buffout Addiction",0x37: "Mentats Addiction",\
          0x38: "Psycho Addiction",0x39: "Radaway Addiction",0x3A: "Weapon Long Range",\
          0x3B: "Weapon Accurate",0x3C: "Weapon Penetrate",0x3D: "Weapon Knockback",0x3E: "Powered Armor",\
          0x3F: "Combat Armor",0x40: "Weapon Scope range",0x41: "Weapon Fast reload",\
          0x42: "Weapon Night sight",0x43: "Weapon Flameboy",0x44: "Armor Advanced I",\
          0x45: "Armor Advanced II",0x46: "Jet Addiction",0x47: "Tragic Addiction",0x48: "Armor Charisma",\
          0x49: "Gecko Skinning",0x4A: "Dermal Impact Armor",0x4B: "Dermal Impact Assault Enhancements",\
          0x4C: "Phoenix Armor Implants",0x4D: "Phoenix Assault Enhancements",\
          0x4E: "Vault City Inoculations",0x4F: "Adrenaline Rush",0x50: "Cautious Nature",\
          0x51: "Comprehension",0x52: "Demolition Expert",0x53: "Gambler",0x54: "Gain Strength",\
          0x55: "Gain Perception",0x56: "Gain Endurance",0x57: "Gain Charisma",0x58: "Gain Intelligence",\
          0x59: "Gain Agility",0x5A: "Gain Luck",0x5B: "Harmless",0x5C: "Here and Now",0x5D: "HtH Evade",\
          0x5E: "Kama Sutra Master",0x5F: "Karma Beacon",0x60: "Light Step",0x61: "Living Anatomy",\
          0x62: "Magnetic Personality",0x63: "Negotiator",0x64: "Pack Rat",0x65: "Pyromaniac",\
          0x66: "Quick Recovery",0x67: "Salesman",0x68: "Stonewall",0x69: "Thief",0x6A: "Weapon Handling",\
          0x6B: "Vault City Training",0x6C: "Alcohol Raised Hit Points",0x6D: "Alcohol Raised Hit Points II",\
          0x6E: "Alcohol Lowered Hit Points",0x6F: "Alcohol Lowered Hit Points II",\
          0x70: "Autodoc Raised Hit Points",0x71: "Autodoc Raised Hit Points II",\
          0x72: "Autodoc Lowered Hit Points",0x73: "Autodoc Lowered Hit Points II",\
          0x74: "Expert Excrement Expeditor",0x75: "Weapon Enhanced Knockout",0x76: "Jinxed" }
