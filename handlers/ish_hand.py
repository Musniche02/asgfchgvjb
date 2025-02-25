from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.state_menu import IShKerakState




ish_router = Router()




@ish_router.message(F.text == "ish kerak")
async def start_ish(msg: Message, state: FSMContext):
    await msg.answer("""
        Ish joyi topish uchun ariza berish

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.          
    """)
    await state.set_state(IShKerakState.malumot)


@ish_router.message(IShKerakState.malumot)
async def start_name(msg: Message, state: FSMContext):
    await state.update_data(malumot=msg.text)
    data = """
          Ism, familiyangizni kiriting?
    """
    await msg.answer(data)
    await state.set_state(IShKerakState.Ism_familiya)



@ish_router.message(IShKerakState.Ism_familiya)
async def get_age(msg: Message, state: FSMContext):
    await state.update_data(ism_familiya=msg.text)
    data = """
       🕑 Yosh: 

Yoshingizni kiriting?
Masalan, 19
"""
    await msg.answer(data)
    await state.set_state(IShKerakState.Yosh)

@ish_router.message(IShKerakState.Yosh)
async def get_texnologiya(msg: Message, state: FSMContext):
    await state.update_data(Yosh=msg.text)
    data = """
    📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#
"""
    await msg.answer(data)
    await state.set_state(IShKerakState.texnologiya)

@ish_router.message(IShKerakState.texnologiya)
async def get_phone(msg: Message, state: FSMContext):
    await state.update_data(texnologiya=msg.text)
    data = """
📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
"""
    await msg.answer(data)
    await state.set_state(IShKerakState.aloqa)

@ish_router.message(IShKerakState.aloqa)
async def get_hudud(msg: Message, state: FSMContext):
    await state.update_data(aloqa=msg.text)
    data = """
🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.
"""
    await msg.answer(data)
    await state.set_state(IShKerakState.hudud)

@ish_router.message(IShKerakState.hudud)
async def get_salary(msg: Message, state: FSMContext):
    await state.update_data(hudud=msg.text)
    data = """
 💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?
"""
    await msg.answer(data)
    await state.set_state(IShKerakState.narx)


@ish_router.message(IShKerakState.narx)
async def get_job(msg: Message, state: FSMContext):
    await state.update_data(narx=msg.text)
    data = """
👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba
"""
    await msg.answer(data)
    await state.set_state(IShKerakState.murojat)

@ish_router.message(IShKerakState.murojat)
async def get_time(msg: Message, state: FSMContext):
    await state.update_data(murojat=msg.text)
    data = """
🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.
"""
    await msg.answer(data)
    await state.set_state(IShKerakState.maqsad)

@ish_router.message(IShKerakState.maqsad)
async def get_chek(msg: Message, state: FSMContext):
    await state.update_data(maqsad=msg.text)
    data = f"""
Sherik kerak:

 


🏅 malumot: {data.get('malumot')}
✍🏾 ism_Familiya: {data.get('ism_familiya')}
📗 Texnologiya: {data.get('texnologiya')}
📞 Aloqa: {data.get('aloqa')}
🌐 Hudud: {data.get('hudud')}
💰 narx: {data.get('narx')}
🕰 Murojaat qilish vaqti: {data.get('murojat')}
🔎maqsad: {data.get('maqsad')}

"""


    await msg.answer(data)
    await state.set_state(IShKerakState.tekshir)