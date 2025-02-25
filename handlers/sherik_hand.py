from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.state_menu import SherikState


sherik_router = Router()


@sherik_router.message(F.text == "Sherik kerak")
async def start_sherik(msg: Message, state: FSMContext):
    await msg.answer("Ism, familiyangizni kiriting?")
    await state.set_state(SherikState.ism_familiya)


@sherik_router.message(SherikState.ism_familiya)
async def get_name(msg: Message, state: FSMContext):
    await state.update_data(ism_familiya=msg.text)
    data = """
📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#

"""
    await msg.answer(data)
    await state.set_state(SherikState.texnologiya)


@sherik_router.message(SherikState.texnologiya)
async def get_phone(msg: Message, state: FSMContext):
    await state.update_data(texnologiya=msg.text)
    data = """
📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
"""
    await msg.answer(data)
    await state.set_state(SherikState.aloqa)

@sherik_router.message(SherikState.aloqa)
async def get_hudud(msg: Message, state: FSMContext):
    await state.update_data(aloqa=msg.text)
    data = """
🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.
"""
    await msg.answer(data)
    await state.set_state(SherikState.hudud)

@sherik_router.message(SherikState.hudud)
async def get_price(msg: Message, state: FSMContext):
    await state.update_data(hudud=msg.text)
    data = """

💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?

"""
    await msg.answer(data)
    await state.set_state(SherikState.narx)


@sherik_router.message(SherikState.narx)
async def get_job(msg: Message, state: FSMContext):
    await state.update_data(narx=msg.text)
    data = """
👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
"""
    await msg.answer(data)
    await state.set_state(SherikState.kasb)

@sherik_router.message(SherikState.kasb)
async def get_time(msg: Message, state: FSMContext):
    await state.update_data(kasb=msg.text)
    data = """
🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
"""
    await msg.answer(data)
    await state.set_state(SherikState.murojat)


@sherik_router.message(SherikState.murojat)
async def get_achive(msg: Message, state: FSMContext):
    await state.update_data(murojat=msg.text)
    data = """
🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.
"""
    await msg.answer(data)
    await state.set_state(SherikState.maqsad)


@sherik_router.message(SherikState.tekshir)
async def get_chek(msg: Message, state: FSMContext):
    await state.update_data(tekshir=msg.text)
    data = f"""
Sherik kerak:

 


🏅 Sherik: {data.get('ism_familiya')}
📚 Texnologiya: {data.get('texnologiya')}
📞 Aloqa: {data.get('aloqa')}
🌐 Hudud: {data.get('hudud')}
💰 Narxi: {data.get('narx')}
👨🏻‍💻 Kasbi: {data.get('kasb')}
🕰 Murojaat qilish vaqti: {data.get('murojat')}
🔎 Maqsad: {data.get('maqsad')}
    
"""


    await msg.answer(data)
    await state.set_state(SherikState.tekshir)





