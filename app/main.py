class Deck:
    def __init__(self, row, column, is_alive=True) -> None:
        self.row = row
        self.column = column
        self.is_alive = is_alive


class Ship:
    def __init__(self, start, end, is_drowned=False) -> None:
        self.start = start
        self.end = end
        self.is_drowned = is_drowned
        self.decks = [Deck(row, column) for row in range(start[0], end[0] + 1) for column in range(start[1], end[1] + 1)]

    def get_deck(self, row, column):
        for deck in self.decks:
            if deck.row == row and deck.column == column:
                return deck
        return None

    def fire(self, row, column) -> None:
        deck = self.get_deck(row, column)
        if deck:
            deck.is_alive = False
            if all(not d.is_alive for d in self.decks):
                self.is_drowned = True


class Battleship:
    def __init__(self, ships) -> None:
        self.field = {}
        for location in ships:
            ship = Ship(location[0], location[1])
            for row in range(location[0][0], location[1][0] + 1):
                for column in range(location[0][1], location[1][1] + 1):
                    self.field[(row, column)] = ship

    def fire(self, location: tuple) -> str:
        if location not in self.field:
            return "Miss!"

        ship = self.field[location]
        ship.fire(location[0], location[1])

        if ship.is_drowned:
            return "Sunk!"
        return "Hit!"
