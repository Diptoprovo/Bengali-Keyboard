import keyboard
from string import ascii_lowercase
from string import ascii_uppercase
import tkinter as tk

# Global variables
eng2beng = {'a':'া',
            'b':'ব',
            'bh':'ভ',
            'c':'চ',
            'ch':'ছ',
            'd':'দ',
            'dh':'ধ',
            'e':'ে',
            'ee':'ী',
            'f':'ফ',
            'g':'গ',
            'gh':'ঘ',
            'h':'',
            'oh':'ঃ',
            'i':'ি',
            'j':'য',
            'jh':'ঝ',
            'k':'ক',
            'kh':'খ',
            'l':'ল',
            'm':'ম',
            'n':'ন',
            'o':'ো',
            'ou':'ৌ',
            'oi':'ৈ',
            'p':'প',
            'ph':'ফ',
            'q':'ঁ',
            'r':'র',
            'Ri':'ৃ',
            's':'স',
            'sh':'শ',
            't':'ত',
            'th':'থ',
            'u':'ু',
            'oo':'ূ',
            'w':'ঙ',
            'x':'শ',
            'y':'য়',
            'z':'্',
            '[':'়',
            'A':'আ',
            'B':'ব',
            'C':'',
            'D':'ড',
            'Dh':'ঢ',
            'E':'এ',
            'EE':'ঈ',
            'F':'',
            'G':'',
            'H':'হ',
            'I':'ই',
            'J':'জ',
            'Jh':'ঝ',
            'K':'',
            'L':'',
            'M':'',
            'N':'ণ',
            'O':'ও',
            'OU':'ঔ',
            'OI':'ঐ',
            'P':'',
            'Q':'অ',
            'R':'র',
            'RI':'ৠ',
            'S':'ষ',
            'T':'ট',
            'Th':'ঠ',
            'U':'উ',
            'OO':'ঊ',
            'V':'',
            'W':'ঞ',
            'X':'',
            'Y':'',
            'Z':'',
            'NG':'ং',
            '1':'১',
            '2':'২',
            '3':'৩',
            '4':'৪',
            '5':'৫',
            '6':'৬',
            '7':'৭',
            '8':'৮',
            '9':'৯',
            '0':'০'
}
ctrl = False
alt = False #alt mode
last = '' #track the last letter pressed
bengali_mode = False  # Track the current mode

# Function to handle key press events
def pressed1(name):
    ch = name.name
    global ctrl
    global alt
    global last

    if ch == 'esc':  # Quit if ESC pressed
        close_app()
        return
    

    if ctrl:  # Check if Ctrl was pressed
        keyboard.press('ctrl+' + ch)
        return
    
    if ch == 'ctrl':
        ctrl = True
        return
    
    if ch == 'alt':
        alt = True
        return
    
    if not bengali_mode:
        keyboard.press(name.name)
        return  # Skip processing if in normal mode
    
    if (last == 'space' or last == '') and ch == 'o':
        keyboard.write(eng2beng['Q'])
        last = ch
        return
    
    if alt:
        if (last + ch) in eng2beng:
            keyboard.press('backspace')
            keyboard.press('backspace')
            keyboard.write(eng2beng[last + ch])
            keyboard.write(eng2beng['z'])
            last = ch
            return
        if ch in eng2beng:
            keyboard.write(eng2beng[ch])
            keyboard.write(eng2beng['z'])
            last = ch
            return

    if (last + ch) in eng2beng:
        keyboard.press('backspace')
        keyboard.write(eng2beng[last + ch])
        last = ch
        return


    if ch == 'Y':
        keyboard.write(eng2beng['z'])
        keyboard.write(eng2beng['y'])
        last = ch
        return

    last = ch


    if ch in eng2beng.keys():
        keyboard.write(eng2beng[ch])
    else:
        keyboard.press(ch)  # Press key if not in eng2beng
    return

# Function to handle key release events
def released1(name):

    ch = name.name
    global ctrl
    global alt
    if ch in eng2beng.keys():  # Keys in eng2beng were suppressed during press event; no need to release
        return

    keyboard.release(ch)  # Release key ch
    if ch == 'ctrl':  # Ctrl is released
        ctrl = False
    if ch == 'alt':  # Alt is released
        alt = False
        keyboard.press('backspace')
    return

# Function to toggle between normal and Bengali modes
def toggle_mode():
    global bengali_mode
    bengali_mode = not bengali_mode
    toggle_button.config(text="Switch to English" if bengali_mode else "Switch to বাংলা")
    print(f"Mode: {'বাংলা' if bengali_mode else 'Normal'}")

# Function to close app and unregister keyboard events
def close_app():
    keyboard.unhook_all()  # Disable all keyboard listeners
    root.destroy()  # Close the tkinter window


# Start keyboard listeners
keyboard.on_press(pressed1, suppress=True)  # Call pressed1 on key press event
keyboard.on_release(released1, suppress=True)  # Call released1 on key release event

# Create a small tkinter window
root = tk.Tk()
root.title("Keyboard Mapper")
root.geometry("300x150")  # Small window size

label = tk.Label(root, text="Keyboard Mapper Running", padx=20, pady=10)
label.pack()

# Toggle button to switch between Normal and Bengali modes
toggle_button = tk.Button(root, text="Switch to বাংলা", command=toggle_mode)
toggle_button.pack(pady=10)

# Close event handler
root.protocol("WM_DELETE_WINDOW", close_app)

# Start tkinter main loop
root.mainloop()  # Keep the tkinter window running

