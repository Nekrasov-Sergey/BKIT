from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

available_city_name = ["Анапа", "Сочи", "Ялта"]
available_day_quantity = ["5", "7", "9"]
available_trip_method = ["самолёт", "поезд", "яхта"]


class OrderTicket(StatesGroup):
    waiting_for_city_name = State()
    waiting_for_day_quantity = State()
    waiting_for_trip_method = State()


async def ticket_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in available_city_name:
        keyboard.add(name)
    await message.answer("Выберите город:", reply_markup=keyboard)
    await OrderTicket.waiting_for_city_name.set()


async def ticket_chosen(message: types.Message, state: FSMContext):
    if ticket_check(message.text):
        await message.answer("В данный город нет билетов, выберите город, используя клавиатуру ниже")
        return
    await state.update_data(chosen_ticket=message.text)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for quantity in available_day_quantity:
        keyboard.add(quantity)
    await OrderTicket.next()
    await message.answer("Теперь выберите количество дней:", reply_markup=keyboard)


async def ticket_quantity_chosen(message: types.Message, state: FSMContext):
    if day_check(message.text):
        await message.answer(
            "На такое количество дней нет билетов, выберите количество дней, используя клавиатуру ниже")
        return
    await state.update_data(chosen_days=message.text)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for method in available_trip_method:
        keyboard.add(method)
    await OrderTicket.next()
    await message.answer("Теперь выберите способ поездки:", reply_markup=keyboard)


async def ticket_method_chosen(message: types.Message, state: FSMContext):
    if trip_check(message.text):
        await message.answer("Такого способа поездки нет, выберите способ поездки, используя клавиатуру ниже")
        return
    user_data = await state.get_data()
    await message.answer(f"Вы отдохнёте {user_data['chosen_days']} дней в городе {user_data['chosen_ticket']}. "
                         f"Ваш способ поездки: {message.text}\n",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


def register_handlers_ticket(dp: Dispatcher):
    dp.register_message_handler(ticket_start, commands="ticket", state="*")
    dp.register_message_handler(ticket_chosen, state=OrderTicket.waiting_for_city_name)
    dp.register_message_handler(ticket_quantity_chosen, state=OrderTicket.waiting_for_day_quantity)
    dp.register_message_handler(ticket_method_chosen, state=OrderTicket.waiting_for_trip_method)


def ticket_check(text):
    if text not in available_city_name:
        return 1
    else:
        return 0


def day_check(text):
    if text not in available_day_quantity:
        return 1
    else:
        return 0


def trip_check(text):
    if text not in available_trip_method:
        return 1
    else:
        return 0
