def user_info(**kwargs):
    return ' '.join(kwargs.values())


print(user_info(Name='Анастасия', Surname='Савина', Birthday='1989', City='Тула', Email='nastyasavin89@mail.ru',
                Phone='8-920-276-63-75'))
