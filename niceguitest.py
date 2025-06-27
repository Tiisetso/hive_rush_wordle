from nicegui import ui
from nicegui.events import ValueChangeEventArguments

ui.add_head_html('''
<style>
  .q-field__control,
  .q-field__control-container,
  .q-field__inner {
    border-radius: 0 !important;
  }
</style>
''')

colors = ['white', 'yellow', 'green']
states = [0] * 5
cells: list[ui.input] = []

def cycle_color(event, idx: int):
    states[idx] = (states[idx] + 1) % len(colors)
    event.sender.style(f'background-color: {colors[states[idx]]}')

def enforce_one_letter(event: ValueChangeEventArguments):
    v = (event.value or '').upper()
    filtered = v[0] if v and v[0].isalpha() else ''
    if event.value != filtered:
        event.sender.value = filtered

def capture_state():
    snapshot = [
        {cell.value.lower() or '': states[i]}
        for i, cell in enumerate(cells)
    ]
    # Additional logic could go here
    print(snapshot)

with ui.row().classes('w-full justify-center').style('margin-top: 5vh'):
    for i in range(5):
        cell = (ui.input()
              .props('maxlength=1 outlined input-class="font-mono h-full w-full"')
              .classes('text-center box-border p-0 rounded-none')
              .style(
                  '--q-field-border-radius: 0; '
                  'width: 55px; '
                  'height: 55px; '
                  'margin: 0px;'
                  'font-size: 24px; '
                  'line-height: 40px; '
                  f'background-color: {colors[0]};'
                  'letter-spacing: 0; '
                  'text-transform: uppercase;'
              )
          .classes('box-border')
          .on('input', enforce_one_letter) 
          .on('click', lambda e, idx=i: cycle_color(e, idx)))
        cells.append(cell)
        
    ui.button('GO', on_click=lambda _: capture_state()).props('unelevated').classes('rounded-none').style('width: 55px; height: 55px; font-size: 16px;')

# data["dict"]
word_counts = {'figgy': 1, 'firms': 1, 'firry': 1, 'fizzy': 1, 'frigs': 1, 'frisk': 1, 'friss': 1, 'frizz': 1, 'gygis': 1, 'griff': 1, 'grigs': 1, 'grimy': 1, 'grimm': 1, 'yirrs': 1, 'immis': 1, 'immix': 1, 'kikki': 1, 'kirks': 1, 'kissy': 1, 'kiwis': 1, 'kriss': 1, 'miffy': 1, 'miffs': 1, 'miggs': 1, 'mikir': 1, 'mimir': 1, 'mimsy': 1, 'mimzy': 1, 'mirky': 1, 'mirks': 1, 'mirvs': 1, 'mysis': 1, 'misky': 1, 'missy': 1, 'mizzy': 1, 'riffi': 1, 'riffs': 1, 'risky': 1, 'risks': 1, 'siris': 1, 'sirki': 1, 'sirky': 1, 'sissy': 1, 'skiff': 1, 'skiis': 1, 'skims': 1, 'skirr': 1, 'skivy': 1, 'skiwy': 1, 'smirk': 1, 'smrgs': 1, 'swigs': 1, 'swimy': 1, 'swims': 1, 'swiss': 1, 'swizz': 1, 'vizir': 1, 'vizzy': 1, 'wiggy': 1, 'xyris': 1, 'xviii': 1, 'xxiii': 1, 'ziffs': 1, 'zimmi': 1, 'zimmy': 1}
words = list(word_counts.keys())

with ui.row().classes('w-full justify-center').style('margin-top: 5vh'):
	with ui.card().style('width: 350px; max-height: 200px; overflow-y: auto;').props('flat'):
		for w in words:
			ui.label(w)

ui.run()
