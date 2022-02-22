description_make_stickers = """
Наші роботи навчилися ходити! Настав час запускати масове виробництво. Щоб роботи на лінії збиралися правильно, потрібно маркувати деталі. Для початку вистачить звичайних наліпок. Різні частини робота будуть складатися з різної кількості деталей.

Напиши програму для принтера make_stickers, яка приймає число details_count і рядок robot_part. Функція повинна повертати список рядків в такому форматі: {robot_part} detail #{n}.

Якщо details_count = 0, поверни порожній список.

Приклади:

make_stickers(3, 'Body') == ['Body detail #1', 'Body detail #2', 'Body detail #3']
make_stickers(4, 'Head') == ['Head detail #1', 'Head detail #2', 'Head detail #3', 'Head detail #4']
"""