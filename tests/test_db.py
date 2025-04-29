from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='Rodrigo',
        email='rodrigo@fast.com',
        password='minha_senha',
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'rodrigo@fast.com')
    )

    assert result.username == 'Rodrigo'
