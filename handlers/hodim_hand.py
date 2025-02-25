from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.state_menu import HodimKerakState

hodim_router = Router()



@hodim_router.message(F.text == "Hodim kerak")
async def start_hodim(msg: Message, state: FSMContext):
    await msg.answer("""
          Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.           
    """)
    await state.set_state(HodimKerakState.malumot)


@hodim_router.message(HodimKerakState.malumot)
async def get_idora(msg: Message, state: FSMContext):
    await state.update_data(malumot=msg.text)
    data = """
        🎓 Idora nomi?
"""
    await msg.answer(data)
    await state.set_state(HodimKerakState.idora)

@hodim_router.message(HodimKerakState.idora)
async def get_texnologiya(msg: Message, state: FSMContext):
    await state.update_data(idora=msg.text)
    data = """
    📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#
"""
    await msg.answer(data)
    await state.set_state(HodimKerakState.texnologiya)


@hodim_router.message(HodimKerakState.texnologiya)
async def get_phone(msg: Message, state: FSMContext):
    await state.update_data(texnologiya=msg.text)
    data = """
📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67
"""
    await msg.answer(data)
    await state.set_state(HodimKerakState.aloqa)

@hodim_router.message(HodimKerakState.aloqa)
async def get_hudud(msg: Message, state: FSMContext):
    await state.update_data(aloqa=msg.text)
    data = """
🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.
"""
    await msg.answer(data)
    await state.set_state(HodimKerakState.hudud)

@hodim_router.message(HodimKerakState.hudud)
async def get_masul(msg: Message, state: FSMContext):
    await state.update_data(hudud=msg.text)
    data = """
 ✍️ Mas'ul ism sharifi?
"""
    await msg.answer(data)
    await state.set_state(HodimKerakState.masul)


@hodim_router.message(HodimKerakState.masul)
async def get_time(msg: Message, state: FSMContext):
    await state.update_data(masul=msg.text)
    data = """
🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00
"""
    await msg.answer(data)
    await state.set_state(HodimKerakState.murojat)

@hodim_router.message(HodimKerakState.murojat)
async def get_work_time(msg: Message, state: FSMContext):
    await state.update_data(murojat=msg.text)
    data = """
🕰 Ish vaqtini kiriting?
"""
    await msg.answer(data)
    await state.set_state(HodimKerakState.ish_vaqt)


@hodim_router.message(HodimKerakState.ish_vaqt)
async def get_salary(msg: Message, state: FSMContext):
    await state.update_data(ish_vaqt=msg.text)
    data = """
💰 Maoshni kiriting?
"""
    await msg.answer(data)
    await state.set_state(HodimKerakState.oylik)

@hodim_router.message(HodimKerakState.oylik)
async def get_q_malumot(msg: Message, state: FSMContext):
    await state.update_data(oylik=msg.text)
    data = """
‼️ Qo`shimcha ma`lumotlar?
"""
    await msg.answer(data)
    await state.set_state(HodimKerakState.qosh_malumot)


@hodim_router.message(HodimKerakState.qosh_malumot)
async def get_chek(msg: Message, state: FSMContext):
    await state.update_data(qosh_malumot=msg.text)
    data = f"""
Sherik kerak:

 


🏅 malumot: {data.get('malumot')}
✍🏾 Idora: {data.get('idora')}
📗 Texnologiya: {data.get('texnologiya')}
📞 Aloqa: {data.get('aloqa')}
🌐 Hudud: {data.get('hudud')}
👨🏻 Mas'ul: {data.get('masul')}
🕰 Murojaat qilish vaqti: {data.get('murojat')}
⏱ Ish_vaqti: {data.get('ish_vaqt')}
💰 Oylik: {data.get('oylik')}
🔎 Qo'shimcha ma'lumot: {data.get('qosh_malumot')}
    
"""


    await msg.answer(data)
    await state.set_state(HodimKerakState.tekshir)










