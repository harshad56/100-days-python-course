from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokeman name", ["pikachu", "salmender", "Charizad"])
table.add_column("type", ["electric", "water", "fire"])
table.align = "l"
print(table)
