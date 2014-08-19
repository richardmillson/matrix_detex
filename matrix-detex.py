
from Tkinter import Tk

def copy(s):
    Tk().clipboard_clear()
    Tk().clipboard_append(s)
    Tk().destroy()

def toMat():
    s = Tk().clipboard_get()
    print s

    if "\\begin{" in s:
        s = s[s.find('}', 0, len(s))+1:]
    if "\\end{" in s:
        s = s[:s.rfind('\\', 0, len(s))]
    s = s.replace(" ", "")
    s = s.replace("\n", "")
    s = s.replace("&", ",")
    s = s.replace("\\\\", "},{")
    s = "{{" + s + "}}"

    print s
    copy(s)

def toTex():
    s = Tk().clipboard_get()
    print s
    
    s = s.replace("{{", "\\begin{bmatrix} \n")
    s = s.replace("}}", "\n\\end{bmatrix}")
    s = s.replace("},{", "\\\\ \n")
    s = s.replace(",", "&")
    
    print s
    copy(s)
