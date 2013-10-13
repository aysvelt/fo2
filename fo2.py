#!/usr/bin/python
from struct import *
from itemlist import *

# http://www.nma-fallout.com/content.php?page=fo-modding-fo-list-itemlist
# http://falloutmods.wikia.com/wiki/SAVE.DAT_File_Format#Inventory_item_format

class InvItem():
    # An item in the players inventory
    # Will need to be expanded for bags, and other variable data
    def __init__(self, id, qty, desc):
        self.id = id
        self.qty = qty
        self.desc = desc


class SaveDat():
        
    def __init__(self, fh):
        self.fh = fh
        self.readHeader()
        self.fpoffset = self.find00FP(self.fh)
        self.readPlayerInfo() # Read in information about the player
        self.readStats() # Read in the player stats field
        self.readKills() # Read in the kill counts
        self.readTagSkills() # Check for tagged skills
        self.readPerks() # Read perks
        
    def hexint(self, twobyteint): return twobyteint[0] * 256 + twobyteint[1]
    
    def hexint4(self, fourbyteint):
        return fourbyteint[0] * 256 * 256 * 256+ fourbyteint[1] * 256 * 256 + fourbyteint[2] * 256 + fourbyteint[3]
    
    def readHeader(self):
        # Make sure we are at the start of the file
        self.fh.seek(0)
        signature = unpack('24s', fh.read(0x18));
        if signature[0] != 'FALLOUT SAVE FILE\x00\x00\x00\x00\x00\x00\x00':
            print "*** Not a save.dat file!"
            return False
    
        self.save_day = [0,0]
        self.save_month = [0,0]
        self.save_year = [0,0]
    
        self.version = unpack ('4B', fh.read(0x04))
        self.fh.read(1) # skip the letter r
        self.player_name, self.save_name,self.save_day[0],self.save_day[1], self.save_month[0],self.save_month[1],\
            self.save_year[0],self.save_year[1] = unpack('32s30s2B2B2B', self.fh.read(0x44))
        
        self.save_day = self.hexint(self.save_day)
        self.save_month = self.hexint(self.save_month)
        self.save_year = self.hexint(self.save_year)
        # Not much more in here worth noting
        
    def find00FP(self, fh):
        
        # Skip towards the end of the header, no need to scan the image
        fh.seek(0x7000)
    
        buffer = []
        count = 0
        while True:
            count = count + 1
            value = unpack('1B', fh.read(1))
            buffer.append(value[0])
    
            if len(buffer) > 3:
                if buffer[-4:] == [0,0,70,80]:
                    offset = fh.tell()
                    break
                else:
                    pass
                    
            # Break eventually...
            if count > 400000:
                print "*** Something has gone wrong, abandoning..."
                return False
        return offset
    
    
    def readPlayerInfo(self):
        self.coordinates = [0,0,0,0]
        self.player_cur_hp = [0,0,0,0]
        self.player_rad_lvl = [0,0,0,0]
        self.player_poison = [0,0,0,0]
        
        self.fh.seek(self.fpoffset)
        self.coordinates[0:3] = unpack('4B',self.fh.read(0x04))
        
        self.fh.read(0x40)
        self.num_items_inv = unpack ('4B', self.fh.read(0x04))
        self.num_items_inv = self.hexint4(self.num_items_inv)
        
        self.fh.read(0x18) # skip unknown
        self.fh.read(0x04)
        self.fh.read(0x0c)
        self.player_cur_hp = self.hexint4(unpack ('4B', self.fh.read(0x04)))
        self.player_rad_lvl = self.hexint4(unpack ('4B', self.fh.read(0x04)))
        self.player_poison = self.hexint4(unpack ('4B', self.fh.read(0x04)))

        self.inventory = []

        for invitem in range(self.num_items_inv):
            # Items come in different sizes, so we need to take the common minimum size, compare
            # the id to lists of item types, and then determine size of its block
            qty = unpack ('4B', self.fh.read(0x04))
            qty = self.hexint4(qty)
            self.fh.read(0x2C)
            id = unpack ('4B', self.fh.read(0x04))
            id = self.hexint4(id)
            
            if id in armor_list:
                extra_field_length = 0x00
            elif id in drug_list:
                extra_field_length = 0x00
            elif id in weapon_list:
                extra_field_length = 0x08
            elif id in container_list:
                extra_field_length = 0x00
            else:
                extra_field_length = 0x04
            
            # Skip 10 non interesting fields, plus any other additional fields
            # this should take us to the start of the next record
            self.fh.read(0x28 + extra_field_length)
            item = InvItem(id,qty,item_names[str(id)])
            self.inventory.append(item)

    def readStats(self):
        # Read in a bunch of stats. Assume you just finished inventory before getting here
        print self.fh.tell()
        self.fh.read(0x0C) # Skip 4 unknown, 4 unknown, 4 tabs
        self.base_stats = {}
        stats = ['strength','perception','endurance','charisma','intelligence','agility','luck',\
                 'hitpoints','actionpoints','armorclass','unused','meleedamage','carryweight','sequence',\
                 'healingrate','criticalchance','hittablerollmodifier']
        for stat in stats:
             self.base_stats[stat] = self.hexint4(unpack ('4B', self.fh.read(0x04)))
        if self.hexint4(unpack ('4B', self.fh.read(0x04))) == 1:
            self.base_stats['gender'] = "female"
        else:
            self.base_stats['gender'] = "male"

        # Skip 35 bonus fields
        self.fh.read(0x8C)
        
        self.skills = {}
        skills = ["small guns", "big guns", "energy weapons", "unarmed", "melee weapons", "throwing"\
                  "first aid", "doctor", "sneak", "lockpick", "steal", "traps", "science", "repair"\
                  "speech", "barter", "gambling", "outdoorsman"]
        for skill in skills:
             self.skills[skill] = self.hexint4(unpack ('4B', self.fh.read(0x04)))
        # Skip another 3 fields, 4/8/4 wide
        self.fh.read(0x10)

    def readKills(self):
        self.kill_counts = {}
        for victim in victim_classes:
            self.kill_counts[victim] = self.hexint4(unpack ('4B', self.fh.read(0x04)))

    def readTagSkills(self):
        # Up to 4 tag skills, mostly will be null
        
        self.tagskills = []

        for i in range(4):
            try:
                self.tagskills.append(skills[self.hexint4(unpack ('4B', self.fh.read(0x04)))])
            except:
                self.tagskills.append("none")

    def readPerks(self):
        # Read in perks
        self.obtained_perks = []
        for i in range(0xB2):
            try:
                self.obtained_perks.append(perks[self.hexint4(unpack ('4B', self.fh.read(0x04)))])
            except:
                self.obtained_perks.append("none")

if __name__ == '__main__':
    fh = open('SAVE.DAT')
    savedat = SaveDat(fh)
    print " ********** GAME INFO ************"
    print "Character's Name: %s" % savedat.player_name
    print "Name of Sav Game: %s" % savedat.save_name
    print "Game's Timestamp: %s" % str(savedat.save_month) + " " + str(savedat.save_day) + " " +  str(savedat.save_year) 
    print "Size of Inventry: %s" % savedat.num_items_inv
    print "Player Currnt HP: %s" % savedat.player_cur_hp
    print "Player Rad Level: %s" % savedat.player_rad_lvl
    print "Player Poisn Lvl: %s" % savedat.player_poison
    print " ********** INVENTORY *************"
    for item in savedat.inventory:
        print str(item.id) + ":", item.qty, item.desc
    print " *********** BASE STATS ************"
    for key in savedat.base_stats.keys():
        print key, savedat.base_stats[key]
    print " *********** SKILLS ***************"
    for key in savedat.skills.keys():
        print key, savedat.skills[key]
    print " ********** KILL COUNTS ***********"
    for key in savedat.kill_counts.keys():
        print key, savedat.kill_counts[key]
    print savedat.tagskills
    print" ************* PERKS ****************"
    for perk in savedat.obtained_perks:
        print perk