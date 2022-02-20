class backEscola():

  def cauculaMedia(self,nota1,nota2,nota3):
    media = (nota1+nota2+nota3)/3
    self.funcaox()
    return media


  def statusMedia(self,media):

    if media >=7:
      return "Passou"
    elif media >=5:
      return "Em Recuepração"
    else:
      return "Reprovado"


  def funcaox(delf):
    print("X")
  
