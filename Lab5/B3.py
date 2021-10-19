class Student:
  def __init__(self, name:str, number: str, course:str, mail:str):
    self.name = name
    self.number = number
    self.course = course
    self.mail = mail
  def __str__(self):
    return ('{}\n{}\n{}\n{} '.format(self.name, self.number, self.course, self.mail))
pupil = Student('TrucPhuong', '187it06944', 'ptran2448@gmail.com', 'K10' )
# a
print(pupil)
