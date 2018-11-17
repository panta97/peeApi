from pyknow import *

class urineColor(Fact):
        """Info about the urine color."""
        pass


class DetectDesease(KnowledgeEngine):
        @Rule(urineColor(colorCode='EFF0F1'))
        def transparent_urineColor(self):
            self.response = 'Usted esta bebiendo mucha agua'

        @Rule(urineColor(colorCode='F4F2DA'))
        def paleStraw_urineColor(self):
            self.response = 'No tiene nada, esta saludable y bien hidratado'

        @Rule(urineColor(colorCode='EFECC1'))
        def transparentYellow_urineColor(self):
            self.response = 'No tiene nada'

        @Rule(urineColor(colorCode='EFECA5'))
        def darkYellow_urineColor(self):
            self.response = 'No tiene nada, pero deberia beber agua pronto'

        @Rule(urineColor(colorCode='E1C98C'))
        def Amber_urineColor(self):
            self.response = 'Su cuerpo no esta recibiendo la suficiente agua, beba un poco ahora'

        @Rule(urineColor(colorCode='AC9F7C'))
        def syrup_urineColor(self):
            self.response = 'Podria tener el higado enfermo o deshidratación severa, beba agua y acuda a su doctor si esto persiste'

        @Rule(urineColor(colorCode='D68E78'))
        def pink_urineColor(self):
            self.response = 'Ha comido remolacha, moras azules o ruibarbo recienteme? Si no es asi, podria tener sangre en su orina. Tal vez no sea nada, o podria tratarse de un tumor, una infección urinaria O problemas de prostata. Contacte a su doctor '

        @Rule(urineColor(colorCode='E4A860'))
        def orange_urineColor(self):
            self.response = 'Tal vez no este bebiendo suficiente agua, tambien podria ser un problema de su conducto biliar. Contacte a su doctor'

        @Rule(urineColor(colorCode='8BC186'))
        def blue_urineColor(self):
            self.response = 'Podria ser una enfermedad genetica, o alguna bacteria que ha infectado su tracto urinario, o simplemente el colorante de alguna comida. Contacte a su doctor si esto persiste'

        @Rule(urineColor(colorCode='DCDD7B'))
        def foaming_urineColor(self):
           self.response = 'Podria ser una exceso de proteina en su dieta o un problema de rinion. Contacte a su doctor si esto persiste'


AI = DetectDesease()