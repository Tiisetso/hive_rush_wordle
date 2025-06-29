from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from filter_dict import *
from letter_frequency import *

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

def cycle_color(event, index: int):
    if not event.sender.value:
        return
    states[index] = (states[index] + 1) % len(colors)
    event.sender.style(f'background-color: {colors[states[index]]}')

def enforce_one_letter(event: ValueChangeEventArguments):
    v = (event.value or '').upper()
    filtered = v[0] if v and v[0].isalpha() else ''
    if event.value != filtered:
        event.sender.value = filtered

def fill_cells(word: str):
    word = word.upper()
    for i, ch in enumerate(word):
        cells[i].value = ch
        states[i] = 0 
        cells[i].style(f'background-color: {colors[0]}')
        cells[i].update()

with ui.row().classes('w-full justify-center').style('margin-top: 5vh'):
    for i in range(5):
        cell = (
            ui.input()
              .props('maxlength=1 outlined input-class="font-mono h-full w-full"')
              .classes('text-center box-border p-0 rounded-none')
              .style(
                  '--q-field-border-radius: 0; '
                  'width: 55px; height: 55px; margin: 0; '
                  'font-size: 24px; line-height: 40px; '
                  f'background-color: {colors[0]}; '
                  'letter-spacing: 0; text-transform: uppercase;'
              )
              .on('input', enforce_one_letter)
              .on('click', lambda e, index=i: cycle_color(e, index))
        )
        cells.append(cell)

    ui.button('GO', on_click=lambda _: capture_state()) \
      .props('unelevated') \
      .classes('rounded-none') \
      .style('width: 55px; height: 55px; font-size: 16px;')

with ui.row().classes('w-full justify-center').style('margin-top: 5vh'):
    word_card = (
        ui.card()
          .props('flat')
          .style(
              'width: 350px; '
              'max-height: 200px; '
              'overflow-y: auto;'
          )
    )

def capture_state():
    snapshot = [
        {cell.value.lower() or '': states[i]}
        for i, cell in enumerate(cells)
    ]
    update_from_guess(data, snapshot)
    # letter_frequency(data)
    # sort_by_letters(data, args.rev)
    
    word_card.clear()
    with word_card:
        with ui.element('div').classes('grid grid-cols-3 gap-2 p-2'):
            for w in data['dict']:
                ui.label(w) \
                  .classes('cursor-pointer') \
                  .on('click', lambda e, w=w: fill_cells(w))

ui.run()
