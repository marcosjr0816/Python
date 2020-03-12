from typing import List

def recite(start_verse: int, end_verse: int) -> List[str]:
    recited_song: List[str] = list()

    for verse_index in range(start_verse, end_verse + 1):
        recited_verse: List[str] = list()

        for line_index in range(0, verse_index):

            items_index = len(ITEMS) - verse_index + line_index
            if line_index == 0:
                name = ITEMS[items_index]["name"]
                action = ITEMS[items_index]["action"]
                that = f' that {action}' if action else ''

                recited_verse.append(f'This is the {name}{that}')
            else:
                name = ITEMS[items_index]["name"]
                action = ITEMS[items_index]["action"]
                that = ' that ' if line_index != verse_index - 1 else ''

                recited_verse.append(f'the {name}{that}{action}')

        recited_song.append(' '.join(recited_verse))

    return recited_song


ITEMS = [
    {'name': 'horse and the hound and the horn', 'action': 'belonged to'},
    {'name': 'farmer sowing his corn', 'action': 'kept'},
    {'name': 'rooster that crowed in the morn', 'action': 'woke'},
    {'name': 'priest all shaven and shorn', 'action': 'married'},
    {'name': 'man all tattered and torn', 'action': 'kissed'},
    {'name': 'maiden all forlorn', 'action': 'milked'},
    {'name': 'cow with the crumpled horn', 'action': 'tossed'},
    {'name': 'dog', 'action': 'worried'},
    {'name': 'cat', 'action': 'killed'},
    {'name': 'rat', 'action': 'ate'},
    {'name': 'malt', 'action': 'lay in'},
    {'name': 'house that Jack built.', 'action': ''},
]
