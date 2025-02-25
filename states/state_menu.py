from aiogram.fsm.state import State, StatesGroup


class SherikState(StatesGroup):
    ism_familiya = State()
    texnologiya = State()
    aloqa = State()
    hudud = State()
    narx = State()
    kasb = State()
    murojat = State()
    maqsad = State()
    tekshir = State()


class UztozKerakState(StatesGroup):
    pass


class ShogirdKerakState(StatesGroup):
    pass


class HodimKerakState(StatesGroup):
    malumot = State()
    idora = State()
    texnologiya = State()
    aloqa = State()
    hudud = State()
    masul = State()
    murojat = State()
    ish_vaqt = State()
    oylik = State()
    qosh_malumot = State()
    tekshir = State()

class IShKerakState(StatesGroup):
    malumot = State()
    Ism_familiya = State()
    Yosh = State()
    texnologiya = State()
    aloqa = State()
    hudud = State()
    narx = State()
    murojat = State()
    maqsad = State()
    tekshir = State()