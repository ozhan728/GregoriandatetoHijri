import jdatetime

class date :
    def __init__(self,year,month,day):

        self.year = year
        self.month = month
        self.day = day

        print(f"Tarikh Miladi : {year} - {month} - {day}")

    def toshamsi(self):
        return jdatetime.date.fromgregorian(day=self.day, month=self.month, year=self.year)

    @classmethod
    def togeorgian(cls,tarikh):
        newtarikh = tarikh.split("-")
        year = newtarikh[0]
        month = newtarikh[1]
        day = newtarikh[2]
        return cls(int(year),int(month),int(day))




newstring = input("Enter daye year-month-date 2000-00-00 : ")
p1 = date.togeorgian(newstring)
print("Tarikh Shamsi : ",p1.toshamsi())
print(f"Tarikh Shamsi 2 : {p1.toshamsi()}")
