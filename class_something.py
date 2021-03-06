
from tkinter import *

grey_color = 'grey'
light_grey_color = 'light grey'
red_color = 'red'
blue_color = 'blue'
green_color = 'green'
yellow_color = 'yellow'

font_type = 'Arial'
font_size = 20
font_kind = 'bold'
font_definitions = (font_type, font_size, font_kind)


root_w = Tk()
#TODO: using for debugging, remove later
root_w.config(bg=light_grey_color)


class EntryFieldForm(Frame):
    def __init__(self, window, entry_field_display_text = None, **kwargs):
        super().__init__(window, **kwargs)

        #TODO: using for debugging, remove later
        self.config(bg=grey_color, borderwidth=5)

        # initializing the widgets inside the frame
        self.text_label = Label(self)
        self.entry_box = Entry(self)

        # Creating a variable to hold the entr widget text
        self.text_variable = StringVar(self.entry_box)

        # changing configuration for widgets
        self.text_label.config(
            font=font_definitions,
            text=entry_field_display_text +": "
        )

        self.entry_box.config(
            font=font_definitions,
            textvariable=self.text_variable
        )

        # placing widgets on the grid inside the frame
        # both on the same row, different columns
        self.text_label.grid(
            row=0,
            column=0,
            sticky=EW,
            padx=(0,10)
        )

        self.entry_box.grid(
            row=0,
            column=1,
            sticky=EW
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0,weight=1)

    def get_entry_text(self):
        return self.text_variable.get()

    def set_entry_text(self, text):
        self.text_variable.set(text)



class FinishingButton(Button):
    def __init__(self, window, button_display_text, **kwargs):
        super().__init__(window, **kwargs)

        #TODO: using for debugging, remove later
        background_color = 'light green'

        border_size = 3

        self.config(
            bg=background_color,
            text=button_display_text,
            borderwidth=border_size,
            font=font_definitions
        )


#TODO: using for debugging, remove later
entry_fields_frame = Frame(root_w, bg=red_color)
entry_fields_frame.config(borderwidth=10)

cnpj_remetente_entry_field = EntryFieldForm(entry_fields_frame, "CNPJ REMETENTE")

cnpj_destino_entry_field= EntryFieldForm(entry_fields_frame, "CNPJ DESTINATARIO")

valor_nota_entry_field = EntryFieldForm(entry_fields_frame, "VALOR DA NOTA")

peso_entry_field = EntryFieldForm(entry_fields_frame, "PESO")

volume_entry_field = EntryFieldForm(entry_fields_frame, "VOLUME")

medidas_entry_field = EntryFieldForm(entry_fields_frame, "MEDIDAS")

pagador_frete_entry_field = EntryFieldForm(entry_fields_frame, "PAGADOR DO FRETE")

entrega_zona_rural_entry_field = EntryFieldForm(entry_fields_frame, "ZONA RURAL")

entry_fields = [
    cnpj_remetente_entry_field,
    cnpj_destino_entry_field,
    valor_nota_entry_field,
    peso_entry_field,
    volume_entry_field,
    medidas_entry_field,
    pagador_frete_entry_field,
    entrega_zona_rural_entry_field
]

for entry_field in entry_fields:
    entry_field_index = entry_fields.index(entry_field)

    entry_field.grid(row=entry_field_index, sticky=EW)
    


#TODO: using for debugging, remove later
buttons_frame = Frame(root_w, borderwidth=5, bg=blue_color)

button_delete = FinishingButton(buttons_frame, "APAGAR")

button_copy = FinishingButton(buttons_frame, "COPIAR")

button_delete.grid(row=0, column=0)
button_copy.grid(row=0, column=1)

buttons_frame.grid_rowconfigure(0, weight=1)
buttons_frame.grid_columnconfigure(0, weight=1)
buttons_frame.grid_columnconfigure(1, weight=1)

entry_fields_frame.grid_columnconfigure(0, weight=1)

entry_fields_frame.grid(row=0, column=0, sticky=EW)
buttons_frame.grid(row=1, column=0, sticky=EW)

root_w.grid_rowconfigure(0, weight=1)
root_w.grid_columnconfigure(0, weight=1)
root_w.grid_rowconfigure(1, weight=1)

root_w.mainloop()
