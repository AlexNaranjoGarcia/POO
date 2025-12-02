import tkinter as tk
from tkcalendar import Calendar

ventana = tk.Tk()
cal = Calendar(ventana, selectmode='day', locale='es_ES', year=2026, month=7, day=1 , date_pattern='y-mm-dd')

cal.pack()

def print_date(date):
    print(date)

cal.bind("<<CalendarSelected>>", lambda e: print_date(cal.get_date()))


ventana.mainloop()



"""





"""