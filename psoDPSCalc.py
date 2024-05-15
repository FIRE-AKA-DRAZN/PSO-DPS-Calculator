# File: my_streamlit_app.py
import streamlit as st

#---DATA---
frameDatav101 = {
    "standard":{
        "Saber":{
            "n1":13,
            "n2":10,
            "n3":31,
            "h1":21,
            "h2":15,
            "h3":34,
        },
        "Sword":{
            "n1":17,
            "n2":15,
            "n3":43,
            "h1":24,
            "h2":19,
            "h3":43,
        },
        "Daggers":{
            "n1":21,
            "n2":15,
            "n3":50,
            "h1":27,
            "h2":20,
            "h3":49,
        },
        "Partisan":{
            "n1":17,
            "n2":14,
            "n3":33,
            "h1":24,
            "h2":19,
            "h3":35,
        },
        "Slicer":{
            "n1":21,
            "n2":12,
            "n3":42,
            "h1":28,
            "h2":17,
            "h3":43,
        },
        "DoubleSaber":{
            "n1":22,
            "n2":11,
            "n3":51,
            "h1":29,
            "h2":16,
            "h3":49,
        },
        "Claw":{
            "n1":16,
            "n2":11,
            "n3":37,
            "h1":24,
            "h2":16,
            "h3":39,
        },
        "Katana":{
            "n1":14,
            "n2":15,
            "n3":44,
            "h1":22,
            "h2":19,
            "h3":44,
        },
        "TwinSwords":{
            "n1":18,
            "n2":19,
            "n3":51,
            "h1":25,
            "h2":22,
            "h3":49,
        },
        "Fists":{
            "n1":19,
            "n2":19,
            "n3":35,
            "h1":26,
            "h2":22,
            "h3":36,
        },
        "Handgun":{
            "n1":14,
            "n2":11,
            "n3":19,
            "h1":22,
            "h2":16,
            "h3":25,
        },
        "Rifle":{
            "n1":15,
            "n2":12,
            "n3":20,
            "h1":23,
            "h2":17,
            "h3":26,
        },
        "Mechguns":{
            "n1":12,
            "n2":10,
            "n3":42,
            "h1":21,
            "h2":15,
            "h3":48,
        },
        "Shot":{
            "n1":25,
            "n2":21,
            "n3":34,
            "h1":31,
            "h2":24,
            "h3":38,
        },
        "Launcher":{
            "n1":21,
            "n2":19,
            "n3":36,
            "h1":27,
            "h2":22,
            "h3":39,
        },
        "Cane":{
            "n1":13,
            "n2":13,
            "n3":39,
            "h1":21,
            "h2":18,
            "h3":40,
        },
        "Rod":{
            "n1":14,
            "n2":14,
            "n3":40,
            "h1":22,
            "h2":19,
            "h3":41,
        },
        "Wand":{
            "n1":14,
            "n2":15,
            "n3":40,
            "h1":21,
            "h2":19,
            "h3":41,
        },
        "Cards":{
            "n1":18,
            "n2":17,
            "n3":47,
            "h1":25,
            "h2":21,
            "h3":47,
        },
        
    },
    "female":{
        "Saber":{
            "n1":13,
            "n2":12,
            "n3":35,
            "h1":21,
            "h2":17,
            "h3":37,
        },
        "DoubleSaber":{
            "n1":18,
            "n2":10,
            "n3":45,
            "h1":25,
            "h2":16,
            "h3":45,
        },
        "Claw":{
            "n1":16,
            "n2":11,
            "n3":34,
            "h1":24,
            "h2":16,
            "h3":36,
        },
        "Katana":{
            "n1":14,
            "n2":15,
            "n3":41,
            "h1":22,
            "h2":19,
            "h3":42,
        },
        "Fists":{
            "n1":18,
            "n2":16,
            "n3":39,
            "h1":25,
            "h2":20,
            "h3":39,
        },
        "Cane":{
            "n1":14,
            "n2":13,
            "n3":39,
            "h1":22,
            "h2":18,
            "h3":40,
        },
        "Rod":{
            "n1":18,
            "n2":17,
            "n3":40,
            "h1":25,
            "h2":21,
            "h3":41,
        }
    },
    
    "hucaseal":{
        "Daggers":{
            "n1":18,
            "n2":14,
            "n3":41,
            "h1":25,
            "h2":18,
            "h3":42,
        },
        "DoubleSaber":{
            "n1":18,
            "n2":11,
            "n3":45,
            "h1":25,
            "h2":16,
            "h3":45,
        },
        "Claw":{
            "n1":21,
            "n2":14,
            "n3":34,
            "h1":27,
            "h2":18,
            "h3":36,
        },
        "Fists":{
            "n1":15,
            "n2":14,
            "n3":36,
            "h1":23,
            "h2":19,
            "h3":38,
        }
    },
    
    "ramarl":{
        "Claw":{
            "n1":21,
            "n2":14,
            "n3":34,
            "h1":27,
            "h2":18,
            "h3":36,
        },
        "Handgun":{
            "n1":13,
            "n2":10,
            "n3":19,
            "h1":21,
            "h2":15,
            "h3":25,
        }
    },
    
    "fomar":{
        "Claw":{
            "n1":21,
            "n2":11,
            "n3":41,
            "h1":27,
            "h2":16,
            "h3":42,
        },
        "Fists":{
            "n1":17,
            "n2":16,
            "n3":45,
            "h1":24,
            "h2":20,
            "h3":45,
        },
        "Rod":{
            "n1":16,
            "n2":14,
            "n3":40,
            "h1":23,
            "h2":19,
            "h3":41,
        },
        "Wand":{
            "n1":14,
            "n2":16,
            "n3":42,
            "h1":21,
            "h2":20,
            "h3":42,
        }
    },
    
    "fomarl":{
        "Saber":{
            "n1":15,
            "n2":12,
            "n3":37,
            "h1":23,
            "h2":17,
            "h3":39,
        },
        "Sword":{
            "n1":16,
            "n2":15,
            "n3":53,
            "h1":23,
            "h2":19,
            "h3":51,
        },
        "Daggers":{
            "n1":23,
            "n2":19,
            "n3":53,
            "h1":29,
            "h2":22,
            "h3":51,
        },
        "Partisan":{
            "n1":16,
            "n2":16,
            "n3":42,
            "h1":24,
            "h2":20,
            "h3":42,
        },
        "Slicer":{
            "n1":20,
            "n2":13,
            "n3":38,
            "h1":26,
            "h2":18,
            "h3":40,
        },
        "DoubleSaber":{
            "n1":21,
            "n2":11,
            "n3":48,
            "h1":27,
            "h2":16,
            "h3":47,
        },
        "Claw":{
            "n1":16,
            "n2":11,
            "n3":34,
            "h1":24,
            "h2":16,
            "h3":36,
        },
        "Katana":{
            "n1":14,
            "n2":15,
            "n3":41,
            "h1":22,
            "h2":19,
            "h3":42,
        },
        "Fists":{
            "n1":17,
            "n2":14,
            "n3":33,
            "h1":24,
            "h2":18,
            "h3":35,
        },
        "Handgun":{
            "n1":17,
            "n2":14,
            "n3":23,
            "h1":24,
            "h2":18,
            "h3":28,
        },
        "Rifle":{
            "n1":17,
            "n2":15,
            "n3":26,
            "h1":24,
            "h2":19,
            "h3":30,
        },
        "Shot":{
            "n1":18,
            "n2":10,
            "n3":27,
            "h1":25,
            "h2":15,
            "h3":32,
        },
        "Rod":{
            "n1":16,
            "n2":14,
            "n3":36,
            "h1":23,
            "h2":19,
            "h3":38,
        },
        "Wand":{
            "n1":14,
            "n2":16,
            "n3":40,
            "h1":21,
            "h2":20,
            "h3":41,
        }
    },
    
    #Special weapons.  
    #Put Seperate anims by class.  
    #If non-comboing, set all values past first as zero.
    "special":{
        "Master Raven":{
            "standard":{
                "n1":26,
                "n2":0,
                "n3":0,
                "h1":36,
                "h2":0,
                "h3":0,
                }
        },
        "L&K38 Combat":{
            "standard":{
                "n1":46,
                "n2":0,
                "n3":0,
                "h1":55,
                "h2":0,
                "h3":0,
            },
            "FOmarl":{
                "n1":45,
                "n2":0,
                "n3":0,
                "h1":54,
                "h2":0,
                "h3":0,
            }
        },
        "Last Swan":{
            "standard":{
                "n1":14,
                "n2":12,
                "n3":21,
                "h1":24,
                "h2":19,
                "h3":28,
            },
            "RAmarl":{
                "n1":14,
                "n2":12,
                "n3":21,
                "h1":24,
                "h2":19,
                "h3":27,
            },
            "FOmarl":{
                "n1":15,
                "n2":12,
                "n3":21,
                "h1":24,
                "h2":19,
                "h3":28,
            }
        },
        "Dark Flow":{
            "standard":{
                "n1":39,
                "n2":0,
                "n3":0,
                "h1":46,
                "h2":0,
                "h3":0,
            }
        }
    }     
}

classAnimMap = {
    "HUmar":{
        "Saber"      :"standard",
        "Sword"      :"standard",
        "Daggers"    :"standard",
        "Partisan"   :"standard",
        "Slicer"     :"standard",
        "DoubleSaber":"standard",
        "Claw"       :"standard",
        "Katana"     :"standard",
        "TwinSwords" :"standard",
        "Fists"      :"standard",
        "Handgun"    :"standard",
        "Rifle"      :"standard",
        "Mechguns"   :"standard",
        "Shot"       :"standard",
        "Launcher"   :"standard",
        "Cane"       :"standard",
        "Rod"        :"standard",
        "Wand"       :"standard",
        "Cards"      :"standard",
    },
    "HUnewearl":{
        "Saber"      :"female",
        "Sword"      :"standard",
        "Daggers"    :"standard",
        "Partisan"   :"standard",
        "Slicer"     :"standard",
        "DoubleSaber":"female",
        "Claw"       :"female",
        "Katana"     :"female",
        "TwinSwords" :"standard",
        "Fists"      :"female",
        "Handgun"    :"standard",
        "Rifle"      :"standard",
        "Mechguns"   :"standard",
        "Shot"       :"standard",
        "Launcher"   :"standard",
        "Cane"       :"standard",
        "Rod"        :"female",
        "Wand"       :"standard",
        "Cards"      :"standard",
    },
    "HUcast":{
        "Saber"      :"standard",
        "Sword"      :"standard",
        "Daggers"    :"standard",
        "Partisan"   :"standard",
        "Slicer"     :"standard",
        "DoubleSaber":"standard",
        "Claw"       :"standard",
        "Katana"     :"standard",
        "TwinSwords" :"standard",
        "Fists"      :"standard",
        "Handgun"    :"standard",
        "Rifle"      :"standard",
        "Mechguns"   :"standard",
        "Shot"       :"standard",
        "Launcher"   :"standard",
        "Cane"       :"standard",
        "Rod"        :"standard",
        "Wand"       :"standard",
        "Cards"      :"standard",
        },
    "HUcaseal":{
        "Saber"      :"female",
        "Sword"      :"standard",
        "Daggers"    :"hucaseal",
        "Partisan"   :"standard",
        "Slicer"     :"standard",
        "DoubleSaber":"hucaseal",
        "Claw"       :"hucaseal",
        "Katana"     :"female",
        "TwinSwords" :"standard",
        "Fists"      :"hucaseal",
        "Handgun"    :"standard",
        "Rifle"      :"standard",
        "Mechguns"   :"standard",
        "Shot"       :"standard",
        "Launcher"   :"standard",
        "Cane"       :"standard",
        "Rod"        :"female",
        "Wand"       :"standard",
        "Cards"      :"standard",
        },
    "RAmar":{
        "Saber"      :"standard",
        "Sword"      :"standard",
        "Daggers"    :"standard",
        "Partisan"   :"standard",
        "Slicer"     :"standard",
        "DoubleSaber":"standard",
        "Claw"       :"standard",
        "Katana"     :"standard",
        "TwinSwords" :"standard",
        "Fists"      :"standard",
        "Handgun"    :"standard",
        "Rifle"      :"standard",
        "Mechguns"   :"standard",
        "Shot"       :"standard",
        "Launcher"   :"standard",
        "Cane"       :"standard",
        "Rod"        :"standard",
        "Wand"       :"standard",
        "Cards"      :"standard",
        },
    "RAmarl":{
        "Saber"      :"female",
        "Sword"      :"standard",
        "Daggers"    :"standard",
        "Partisan"   :"standard",
        "Slicer"     :"standard",
        "DoubleSaber":"female",
        "Claw"       :"ramarl",
        "Katana"     :"female",
        "TwinSwords" :"standard",
        "Fists"      :"female",
        "Handgun"    :"ramarl",
        "Rifle"      :"standard",
        "Mechguns"   :"standard",
        "Shot"       :"standard",
        "Launcher"   :"standard",
        "Cane"       :"standard",
        "Rod"        :"female",
        "Wand"       :"standard",
        "Cards"      :"standard",
        },
    "RAcast":{
        "Saber"      :"standard",
        "Sword"      :"standard",
        "Daggers"    :"standard",
        "Partisan"   :"standard",
        "Slicer"     :"standard",
        "DoubleSaber":"standard",
        "Claw"       :"standard",
        "Katana"     :"standard",
        "TwinSwords" :"standard",
        "Fists"      :"standard",
        "Handgun"    :"standard",
        "Rifle"      :"standard",
        "Mechguns"   :"standard",
        "Shot"       :"standard",
        "Launcher"   :"standard",
        "Cane"       :"standard",
        "Rod"        :"standard",
        "Wand"       :"standard",
        "Cards"      :"standard",
        },
    "RAcaseal":{
        "Saber"      :"female",
        "Sword"      :"standard",
        "Daggers"    :"standard",
        "Partisan"   :"standard",
        "Slicer"     :"standard",
        "DoubleSaber":"female",
        "Claw"       :"female",
        "Katana"     :"female",
        "TwinSwords" :"standard",
        "Fists"      :"female",
        "Handgun"    :"standard",
        "Rifle"      :"standard",
        "Mechguns"   :"standard",
        "Shot"       :"standard",
        "Launcher"   :"standard",
        "Cane"       :"standard",
        "Rod"        :"female",
        "Wand"       :"standard",
        "Cards"      :"standard",
        },
    "FOmar":{
        "Saber"      :"standard",
        "Sword"      :"standard",
        "Daggers"    :"standard",
        "Partisan"   :"standard",
        "Slicer"     :"standard",
        "DoubleSaber":"standard",
        "Claw"       :"fomar",
        "Katana"     :"standard",
        "TwinSwords" :"standard",
        "Fists"      :"fomar",
        "Handgun"    :"standard",
        "Rifle"      :"standard",
        "Mechguns"   :"standard",
        "Shot"       :"standard",
        "Launcher"   :"standard",
        "Cane"       :"standard",
        "Rod"        :"fomar",
        "Wand"       :"fomar",
        "Cards"      :"standard",
        },
    "FOmarl":{
        "Saber"      :"fomarl",
        "Sword"      :"fomarl",
        "Daggers"    :"fomarl",
        "Partisan"   :"fomarl",
        "Slicer"     :"fomarl",
        "DoubleSaber":"fomarl",
        "Claw"       :"fomarl",
        "Katana"     :"fomarl",
        "TwinSwords" :"standard",
        "Fists"      :"fomarl",
        "Handgun"    :"fomarl",
        "Rifle"      :"fomarl",
        "Mechguns"   :"standard",
        "Shot"       :"fomarl",
        "Launcher"   :"standard",
        "Cane"       :"standard",
        "Rod"        :"fomarl",
        "Wand"       :"fomarl",
        "Cards"      :"standard",
        },
    "FOnewm":{
        "Saber"      :"standard",
        "Sword"      :"standard",
        "Daggers"    :"standard",
        "Partisan"   :"standard",
        "Slicer"     :"standard",
        "DoubleSaber":"standard",
        "Claw"       :"standard",
        "Katana"     :"standard",
        "TwinSwords" :"standard",
        "Fists"      :"standard",
        "Handgun"    :"standard",
        "Rifle"      :"standard",
        "Mechguns"   :"standard",
        "Shot"       :"standard",
        "Launcher"   :"standard",
        "Cane"       :"standard",
        "Rod"        :"standard",
        "Wand"       :"standard",
        "Cards"      :"standard",
        },
    "FOnewearl":{
        "Saber"      :"female",
        "Sword"      :"standard",
        "Daggers"    :"standard",
        "Partisan"   :"standard",
        "Slicer"     :"standard",
        "DoubleSaber":"female",
        "Claw"       :"female",
        "Katana"     :"female",
        "TwinSwords" :"standard",
        "Fists"      :"female",
        "Handgun"    :"standard",
        "Rifle"      :"standard",
        "Mechguns"   :"standard",
        "Shot"       :"standard",
        "Launcher"   :"standard",
        "Cane"       :"standard",
        "Rod"        :"female",
        "Wand"       :"standard",
        "Cards"      :"standard",
        },
}

wepTypeList = [
    "Saber","Sword","Daggers","Partisan","Slicer","DoubleSaber","Claw","Katana","TwinSwords","Fists","Handgun","Rifle","Mechguns","Shot","Launcher","Cane","Rod","Wand","Cards","Master Raven","Last Swan","L&K38 Combat","Dark Flow" 
]

techBoost = [
    0,
    10,
    11.3,
    12.6,
    13.9,
    15.2,
    16.5,
    17.8,
    18.1,
    20.4,
    21.7,
    23,
    24.3,
    25.6,
    26.9,
    28.2,
    29.5,
    30.8,
    32.1,
    33.4,
    34.7,
    36,
    37.3,
    38.6,
    39.9,
    41.2,
    42.5,
    43.8,
    45.1,
    46.4,
    47.7,
]

attackMod = {
    "Normal":0.9,
    "Heavy":1.89,
    "Special":0.56,
    "Sacrificial":3.33,
    "Vjaya":5.67
}

accTypeMod = {
    "Normal":1,
    "Heavy":0.7,
    "Special":0.5,
    "Sacrificial":0.5,
    "Vjaya":0.5
}

accStepMod = [1.0, 1.3, 1.69]

comboPattern = {
    "Saber":[1,1,1],
    "Sword":[1,1,1],
    "Daggers":[2,2,2],
    "Partisan":[1,1,1],
    "Slicer":[1,1,1],
    "DoubleSaber":[2,1,3],
    "Claw":[1,1,1],
    "Katana":[1,1,1],
    "TwinSwords":[2,1,3],
    "Fists":[1,1,1],
    "Handgun":[1,1,1],
    "Rifle":[1,1,1],
    "Mechguns":[3,3,3],
    "Shot":[1,1,1],
    "Launcher":[1,1,1],
    "Cane":[1,1,1],
    "Rod":[1,1,1],
    "Wand":[1,1,1],
    "Cards":[1,1,3],
    "Master Raven":[3,0,0],
    "Last Swan":[3,3,3],
    "L&K38 Combat":[5,0,0],
    "Dark Flow":[1,0,0],
}

classList = list(classAnimMap.keys())

#---FUNC---
def find_anim(player, wep):
    animSet = classAnimMap.get(player)
    
    if animSet.get(wep) is not None:
    #Not special, treat normally    
        animName = animSet.get(wep)
        wepAnims = frameDatav101.get(animName)
        return wepAnims.get(wep)
    else:
    #Is special, find specifics        
        special = frameDatav101.get("special")
        specWep = special.get(wep)
        if player in specWep:
            specAnims = specWep.get(player)
        else:
            specAnims = specWep.get("standard")
            #print(wepAnims)
        return specAnims

def convert_combo_input(combo):
    output = []
    timing = 1
    for c in combo:
        if c is "Normal":
            output.append(f"n{timing}")
        else:
            output.append(f"h{timing}")
        timing = timing+1
    #st.write(output)
    return output

def find_combo_time(player, wep):
    combo = convert_combo_input([wep["a1"],wep["a2"],wep["a3"]])
    frames = find_anim(player["playerClass"], wep["type"])
    
    totalTime = 0
    for f in frames:
        if f in combo:
            totalTime = totalTime+frames.get(f)
    return totalTime

def dmg_calc(base, enemy, wep, combo, step):
    #Find how many hits are in the combo step
    comboHits = comboPattern[wep["type"]][step]
    
    #Min weapon ATP, and Frame/Barrier flat ATP boosts, are unscaled by Shifta but are improved by attributes
    minATP = wep["minATP"]*(1+(wep["ATR"]/100))
    maxATP = wep["maxATP"]*(1+(wep["ATR"]/100))
    otherATP = base["otherATP"]*(1+(wep["ATR"]/100))
    
    unscaledATP = minATP+otherATP
    #Take average of weapon ATP range and base ATP, then multiply it by the correct Shifta boost if any
    scaledATPmin = base["ATP"] * (1 + (techBoost[base["shifta"]]/100) )
    scaledATPmax = ( ( (maxATP-minATP)) + int(base["ATP"]) ) * (1 + (techBoost[base["shifta"]]/100) )
    
    finalATPmin = unscaledATP+scaledATPmin
    finalATPmax = unscaledATP+scaledATPmax
    
    #DFP is reduced uniformly by Zalure
    targetDFP = int(enemy["DFP"]) * (1-(techBoost[base["zalure"]]/100))
    
    #ATP is reduced directly by DFP.  The result is then divided by 5, then the attack's multiplier is added to produce the final damage
    if wep["type"] is "Dark Flow" and combo in ["Special","Sacrificial","Vjaya"]:
        baseDamageMin = (((finalATPmin-targetDFP)/5) * attackMod["Heavy"])*5
        baseDamageMax = (((finalATPmax-targetDFP)/5) * attackMod["Heavy"])*5
    else:
        baseDamageMin = (((finalATPmin-targetDFP)/5) * attackMod[combo])*comboHits
        baseDamageMax = (((finalATPmax-targetDFP)/5) * attackMod[combo])*comboHits
    
    #The average damage boost from crit for a 100 luck character will be 12.5%
    avgCritMulti = (0.5*((int(base["luck"])/5)/100))
    avgDamage = int( ( (baseDamageMin+baseDamageMax)/2 ) * (1+avgCritMulti) )
    
    results = [int(baseDamageMin),int(baseDamageMax),int(avgDamage)]
    
    #return the average damage
    return results

def acc_calc(base, enemy, wep, combo, step):
    if wep["type"] is "Dark Flow" and combo in ["Special","Sacrificial","Vjaya"]:
        typeMod = accTypeMod["Heavy"]
    else:
        typeMod = accTypeMod[combo]
    
    stepMod = accStepMod[step]
    
    totalATA = int(base["ATA"]) + int(wep["ATA"])
    
    comboATA = totalATA * typeMod * stepMod
    
    enemyEVP = enemy["EVP"]

    if "Paralysed" in enemy["state"] or "Shocked" in enemy["state"]:
            enemyEVP = enemyEVP * 0.85
            
    if "Frozen" in enemy["state"]:
                enemyEVP = enemyEVP * 0.7     

    result = comboATA - (enemyEVP/5)
    
    if result > 100:
        return 100
    
    if result < 0:
        return 0
    
    return result

def dps_calc(dmg, acc, time):
    fullDamage = (dmg[0]*(acc[0]/100))+(dmg[1]*(acc[1]/100))+(dmg[2]*(acc[2]/100))
    
    dps = fullDamage / (time/30)
    
    return dps

#---MAIN---
def main():
    st.title("Phantasy Star Online DPS Calculator")
    st.markdown("[Please visit the PSO Ephinea wiki for vanilla PSO enemy, weapon and class stats](https://wiki.pioneer2.net/w/Main_Page)")
    #---SIDEBAR---
    st.sidebar.title("Extra Configs")
    with st.sidebar.expander("Enemy Config",expanded=True):
        enemyHP = st.number_input("HP",0,value=3000)
        enemyState=st.multiselect("Enemy State",["Frozen","Paralysed","Shocked"],placeholder="Normal")
        # enemyType = st.selectbox("Type",["Native","A-Beast","Machine","Dark"])
        enemyDFP = st.number_input("DFP",0,value=802)
        enemyEVP = st.number_input("EVP",0,value=712)
        enemyFire = st.slider("EFR",0,100,50)
        enemyCold = st.slider("EIC",0,100,100)
        enemyElec = st.slider("ETH",0,100,78)
        enemyLight = st.slider("ELT",0,100,65)
        
    with st.sidebar.expander("Misc Config",expanded=True):
        otherATP = st.number_input("Other ATP bonuses (Frame, Barrier etc)",0)
        
    st.sidebar.write("*All attack timings assume you have a 40% attack speed boost from a Heavenly/Battle or v101")
    st.sidebar.text("Created By: FIRE AKA Drazn")
    
    #---MAIN WINDOW---  
        
    col1, col2, col3 = st.columns(3)            

    with col1:        
        playerClass = st.selectbox("Class", classList)
        shifta = st.slider("Shifta", 0 , 30)
        
        with st.expander("Weapon 1 Results",expanded=True):
            w1DPS = st.header(f"1,000 DPS")
            w1ComboDamage = st.text("Full Combo: ")
            w1ComboTime = st.text("Combo Time: ")
            w1A1result = st.text(f"")
            w1A2result = st.text(f"")
            w1A3result = st.text(f"")
            
        with st.expander("Weapon 1 Combo Selector",expanded=False):            
            w1A1=st.selectbox("Weapon 1 First Attack",["Normal","Heavy","Special","Sacrificial","Vjaya"])
            w1A2=st.selectbox("Weapon 1 Second Attack",["Normal","Heavy","Special","Sacrificial","Vjaya"])
            w1A3=st.selectbox("Weapon 1 Third Attack",["Normal","Heavy","Special","Sacrificial","Vjaya"])
            
        with st.expander("Weapon 1 Config",expanded=True):
            w1Type=st.selectbox("Weapon 1 Type",wepTypeList)
            w1ATPmin=st.number_input("Weapon 1 Min ATP",0,value=240)
            w1ATPmax=st.number_input("Weapon 1 Max ATP",0,value=280)
            w1ATA=st.number_input("Weapon 1 ATA",0,value=40)
            w1ATR=st.slider("Weapon 1 Attribute vs Enemy",0,100,0,5)

    with col2:
        baseATP=st.number_input("Base ATP",0,value=1397)
        baseLuck=st.slider("Luck",10,100,100)
        
        with st.expander("Weapon 2 Results",expanded=True):
            w2DPS = st.header(f"1,000 DPS")
            w2ComboDamage = st.text("Full Combo: ")
            w2ComboTime = st.text("Combo Time: ")
            w2A1result = st.text(f"")
            w2A2result = st.text(f"")
            w2A3result = st.text(f"")
            
        with st.expander("Weapon 2 Combo Selector",expanded=False):
            w2A1=st.selectbox("Weapon 2 First Attack",["Normal","Heavy","Special","Sacrificial","Vjaya"])
            w2A2=st.selectbox("Weapon 2 Second Attack",["Normal","Heavy","Special","Sacrificial","Vjaya"])
            w2A3=st.selectbox("Weapon 2 Third Attack",["Normal","Heavy","Special","Sacrificial","Vjaya"])
            
        with st.expander("Weapon 2 Config",expanded=True):
            w2Type=st.selectbox("Weapon 2 Type",wepTypeList)
            w2ATPmin=st.number_input("Weapon 2 Min ATP",0,value=240)
            w2ATPmax=st.number_input("Weapon 2 Max ATP",0,value=280)
            w2ATA=st.number_input("Weapon 2 ATA",0,value=40)
            w2ATR=st.slider("Weapon 2 Attribute vs Enemy",0,100,0,5)


    with col3:
        baseATA=st.number_input("Base ATA",0,value=200)
        zalure = st.slider("Zalure", 0 , 30)
        
        with st.expander("Weapon 3 Results",expanded=True):
            w3DPS = st.header(f"1,000 DPS")
            w3ComboDamage = st.text("Full Combo: ")
            w3ComboTime = st.text("Combo Time: ")
            w3A1result = st.text(f"")
            w3A2result = st.text(f"")
            w3A3result = st.text(f"")
            
        with st.expander("Weapon 3 Combo Selector",expanded=False):
            w3A1=st.selectbox("Weapon 3 First Attack",["Normal","Heavy","Special","Sacrificial","Vjaya"])
            w3A2=st.selectbox("Weapon 3 Second Attack",["Normal","Heavy","Special","Sacrificial","Vjaya"])
            w3A3=st.selectbox("Weapon 3 Third Attack",["Normal","Heavy","Special","Sacrificial","Vjaya"])
            
        with st.expander("Weapon 3 Config",expanded=True):
            w3Type=st.selectbox("Weapon 3 Type",wepTypeList)
            w3ATPmin=st.number_input("Weapon 3 Min ATP",0,value=240)
            w3ATPmax=st.number_input("Weapon 3 Max ATP",0,value=280)
            w3ATA=st.number_input("Weapon 3 ATA",0,value=40)
            w3ATR=st.slider("Weapon 3 Attribute vs Enemy",0,100,0,5)

    #---VARS---
    basePack = {
        "playerClass":playerClass,
        "ATP":int(baseATP),
        "otherATP":int(otherATP),
        "ATA":int(baseATA),
        "luck":int(baseLuck),
        "shifta":int(shifta),
        "zalure":int(zalure),
    }
    enemyPack = {
        "HP":int(enemyHP),
        "state":enemyState,
        "DFP":int(enemyDFP),
        "EVP":int(enemyEVP),
        "EFR":int(enemyFire),
        "EIC":int(enemyCold),
        "ETH":int(enemyElec),
        "ELT":int(enemyLight),
    }
    w1Pack = {
        "type":w1Type,
        "minATP":int(w1ATPmin),
        "maxATP":int(w1ATPmax),
        "ATA":int(w1ATA),     
        "ATR":int(w1ATR),
        "combo":comboPattern[w1Type],
        "a1":w1A1,
        "a2":w1A2,
        "a3":w1A3,
    }
    w2Pack = {
        "type":w2Type,
        "minATP":int(w2ATPmin),
        "maxATP":int(w2ATPmax),
        "ATA":int(w2ATA),     
        "ATR":int(w2ATR),
        "combo":comboPattern[w2Type],
        "a1":w2A1,
        "a2":w2A2,
        "a3":w2A3,
    }
    w3Pack = {
        "type":w3Type,
        "minATP":int(w3ATPmin),
        "maxATP":int(w3ATPmax),
        "ATA":int(w3ATA),     
        "ATR":int(w3ATR),
        "combo":comboPattern[w3Type],
        "a1":w3A1,
        "a2":w3A2,
        "a3":w3A3,
    }

    #---CALCS---   
    
    #Wep 1
    w1A1Dmg = dmg_calc(basePack,enemyPack,w1Pack,w1Pack["a1"],0)
    w1A1Acc = acc_calc(basePack,enemyPack,w1Pack,w1Pack["a1"],0)
    if w1A1Dmg[2] > 0:
        w1A1result.write(f"1 | {w1A1Acc:.0f}% | {w1A1Dmg[0]} to {w1A1Dmg[1]}")
    

    w1A2Dmg = dmg_calc(basePack,enemyPack,w1Pack,w1Pack["a2"],1)
    w1A2Acc = acc_calc(basePack,enemyPack,w1Pack,w1Pack["a2"],1)
    if w1A2Dmg[2] > 0:
        w1A2result.write(f"2 | {w1A2Acc:.0f}% | {w1A2Dmg[0]} to {w1A2Dmg[1]}")


    w1A3Dmg = dmg_calc(basePack,enemyPack,w1Pack,w1Pack["a3"],2)
    w1A3Acc = acc_calc(basePack,enemyPack,w1Pack,w1Pack["a3"],2)
    if w1A3Dmg[2] > 0:    
        w1A3result.write(f"3 | {w1A3Acc:.0f}% | {w1A3Dmg[0]} to {w1A3Dmg[1]}")
    
    w1ComboDamage.write(f"Full Combo: {w1A1Dmg[0]+w1A2Dmg[0]+w1A3Dmg[0]} to {w1A1Dmg[1]+w1A2Dmg[1]+w1A3Dmg[1]}")
    w1Time=find_combo_time(basePack, w1Pack)
    w1ComboTime.text(f"Combo Time: {w1Time/30:.1f} sec")
    w1DPS.header(f"DPS: {dps_calc([w1A1Dmg[2],w1A2Dmg[2],w1A3Dmg[2]],[w1A1Acc,w1A2Acc,w1A3Acc],w1Time):.0f}")
    
    #Wep 2
    w2A1Dmg = dmg_calc(basePack,enemyPack,w2Pack,w2Pack["a1"],0)
    w2A1Acc = acc_calc(basePack,enemyPack,w2Pack,w2Pack["a1"],0)
    if w2A1Dmg[2] > 0:
        w2A1result.write(f"1 | {w2A1Acc:.0f}% | {w2A1Dmg[0]} to {w2A1Dmg[1]}")
    
    
    w2A2Dmg = dmg_calc(basePack,enemyPack,w2Pack,w2Pack["a2"],1)
    w2A2Acc = acc_calc(basePack,enemyPack,w2Pack,w2Pack["a2"],1)
    if w2A2Dmg[2] > 0:
        w2A2result.write(f"2 | {w2A2Acc:.0f}% | {w2A2Dmg[0]} to {w2A2Dmg[1]}")


    w2A3Dmg = dmg_calc(basePack,enemyPack,w2Pack,w2Pack["a3"],2)
    w2A3Acc = acc_calc(basePack,enemyPack,w2Pack,w2Pack["a3"],2)
    if w2A3Dmg[2] > 0:
        w2A3result.write(f"3 | {w2A3Acc:.0f}% | {w2A3Dmg[0]} to {w2A3Dmg[1]}")
        
    w2ComboDamage.write(f"Full Combo: {w2A1Dmg[0]+w2A2Dmg[0]+w2A3Dmg[0]} to {w2A1Dmg[1]+w2A2Dmg[1]+w2A3Dmg[1]}")
    w2Time=find_combo_time(basePack, w2Pack)
    w2ComboTime.text(f"Combo Time: {w2Time/30:.1f} sec")
    w2DPS.header(f"DPS: {dps_calc([w2A1Dmg[2],w2A2Dmg[2],w2A3Dmg[2]],[w2A1Acc,w2A2Acc,w2A3Acc],w2Time):.0f}")
    
    #Wep 3
    w3A1Dmg = dmg_calc(basePack,enemyPack,w3Pack,w3Pack["a1"],0)
    w3A1Acc = acc_calc(basePack,enemyPack,w3Pack,w3Pack["a1"],0)
    if w3A1Dmg[2] > 0:
        w3A1result.write(f"1 | {w3A1Acc:.0f}% | {w3A1Dmg[0]} to {w3A1Dmg[1]}")
    

    w3A2Dmg = dmg_calc(basePack,enemyPack,w3Pack,w3Pack["a2"],1)
    w3A2Acc = acc_calc(basePack,enemyPack,w3Pack,w3Pack["a2"],1)
    if w3A2Dmg[2] > 0:    
        w3A2result.write(f"2 | {w3A2Acc:.0f}% | {w3A2Dmg[0]} to {w3A2Dmg[1]}")
    

    w3A3Dmg = dmg_calc(basePack,enemyPack,w3Pack,w3Pack["a3"],2)
    w3A3Acc = acc_calc(basePack,enemyPack,w3Pack,w3Pack["a3"],2)
    if w3A3Dmg[2] > 0:    
        w3A3result.write(f"3 | {w3A3Acc:.0f}% | {w3A3Dmg[0]} to {w3A3Dmg[1]}")
    
    w3ComboDamage.write(f"Full Combo: {w3A1Dmg[0]+w3A2Dmg[0]+w3A3Dmg[0]} to {w3A1Dmg[1]+w3A2Dmg[1]+w3A3Dmg[1]}")
    w3Time=find_combo_time(basePack, w3Pack)
    w3ComboTime.text(f"Combo Time: {w3Time/30:.1f} sec")
    w3DPS.header(f"DPS: {dps_calc([w3A1Dmg[2],w3A2Dmg[2],w3A3Dmg[2]],[w3A1Acc,w3A2Acc,w3A3Acc],w3Time):.0f}")
    
    #---FOOTER---
    
    
#---END---
if __name__ == "__main__":
    main()