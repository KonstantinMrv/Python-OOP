class Player:

    def __init__(self, name, hp, mp):
        self.mp = mp
        self.hp = hp
        self.name = name
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        skills_info = "\n".join([f"==={skill_name} - {mana_cost}" for skill_name, mana_cost in self.skills.items()])
        return f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n{skills_info}"



