class Top:
    def m_top(self):
        print("top")

class Middle(Top):
    def m_middle(self):
        print("middle")

class Bottom(Top, Middle):
    def m_bottom(self):
        print("bottom")

object = Bottom()
object.m_bottom()  # Salida esperada: bottom
object.m_middle()  # Salida esperada: middle
object.m_top()     # Salida esperada: top
