
# Изменяем оценку
def change_rate(number,rate,form):
    number = int(number)
    rate.rate = number
    form.lesson = rate.lesson
    rate.save()



