from pyreact import useState, createElement, Component

# This File is a copy of front.js from the frontend
# made to reduce the amount of data in the app
# once this is completed we can delete Stats.js and Types.js
# These two are a redundancy


# Import the necessary data from Stats and Types modules
from Stats import statData
from Types import typeData

class PokemonDropdown(Component):
    def __init__(self):
        super().__init__()
        self.selectedPokemon, set_selectedPokemon = useState("MissingNo.")
        self.selectedID, set_selectedID = useState("")
        self.selectedTotal, set_selectedTotal = useState("")
        self.selectedHP, set_selectedHP = useState("")
        self.selectedAttack, set_selectedAttack = useState("")
        self.selectedDef, set_selectedDef = useState("")
        self.selectedSpA, set_selectedSpA = useState("")
        self.selectedSpD, set_selectedSpD = useState("")
        self.selectedSpeed, set_selectedSpeed = useState("")
        self.selectedType1, set_selectedType1 = useState("")
        self.selectedType2, set_selectedType2 = useState("")

        def handleSelectChange(event):
            ID = event.target.value
            print(ID)
            set_selectedID(ID)
            set_selectedPokemon(statData[ID]["Name"])
            set_selectedTotal(statData[ID]["Total"])
            set_selectedHP(statData[ID]["HP"])
            set_selectedAttack(statData[ID]["Attack"])
            set_selectedDef(statData[ID]["Defense"])
            set_selectedSpA(statData[ID]["SpAtk"])
            set_selectedSpD(statData[ID]["SpDef"])
            set_selectedSpeed(statData[ID]["Speed"])
            # Adding type
            set_selectedType1(typeData[ID][0])
            set_selectedType2(typeData[ID][1])

        self.handleSelectChange = handleSelectChange

    def render(self):
        return (
            createElement("div", {"class": "dropdown"}, [
                createElement("label", {"for": "pokemonSelect"}),
                createElement("select", {"id": "pokemonSelect", "onChange": self.handleSelectChange, "value": self.selectedPokemon}, [
                    createElement("option", {"value": ""}, self.selectedPokemon),
                    *[createElement("option", {"key": id, "value": id}, statData[id]["Name"]) for id in statData],
                ]),
                createElement("div", None, [
                    createElement("div", None, f"Selected Pokemon: {self.selectedPokemon}"),
                    createElement("div", None, f"Total: {self.selectedTotal}"),
                    createElement("div", None, f"ID: {self.selectedID}"),
                    createElement("div", {"class": "statsholder"}, [
                        createElement("div", {"class": "col"}, [
                            createElement("div", None, f"HP: {self.selectedHP}"),
                            createElement("div", None, f"Attack: {self.selectedAttack}"),
                            createElement("div", None, f"Defense: {self.selectedDef}"),
                        ]),
                        createElement("div", {"class": "col"}, [
                            createElement("div", None, f"SpAtk: {self.selectedSpA}"),
                            createElement("div", None, f"SpDef: {self.selectedSpD}"),
                            createElement("div", None, f"Speed: {self.selectedSpeed}"),
                        ]),
                        createElement("div", None),
                    ]),
                    createElement("div", {"class": "typeholder"}, [f"{self.selectedType1} {self.selectedType2}"]),
                ]),
            ])
        )

# Export the component as the default
export = PokemonDropdown