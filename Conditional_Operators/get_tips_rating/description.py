description_get_tips_rating = """
Усі офіціанти люблять чайові та навіть оцінюють їх відповідно до секретного рейтингу!

Реалізуй функцію get_tips_rating, яка приймає суму чайових amount та повертає рядок-оцінку відповідно до залишеної суми:

terrible, якщо amount дорівнює 0 грн;
poor, якщо amount від 0 до 10 грн включно;
good, якщо amount від 10 до 20 грн включно;
great, якщо amount від 20 до 50 грн включно;
excellent, якщо amount більше 50 грн.
Приклад:

def get_tips_rating(amount):
    if amount == 0:
        return "terrible"
    if amount <= 10:
        return "poor"

  # add other conditions...


get_tips_rating(0) == 'terrible'
get_tips_rating(1) == 'poor'
get_tips_rating(10) == 'poor'
"""