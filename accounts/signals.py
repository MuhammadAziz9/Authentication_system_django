# import random
# import string

# # 1. Foydalanuvchidan ism va yoshni olish
# def get_user_info():
#     name = input("Ismingizni kiriting: ")
#     age = int(input("Yoshingizni kiriting: "))
#     return name, age

# # 2. Tasodifiy parol yaratish funksiyasi
# def generate_random_password(length=12):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for i in range(length))
#     return password

# # 3. Foydalanuvchi ma'lumotlarini tekshirish
# def validate_user_age(age):
#     if age < 18:
#         return "Siz juda yoshsiz, kirish uchun 18 yoshdan katta bo'lishingiz kerak."
#     elif age >= 18 and age < 60:
#         return "Siz o'rta yoshdasiz, tizimga kirishingiz mumkin."
#     else:
#         return "Siz keksa yoshsiz, tizimga kirishingiz mumkin."

# # 4. Foydalanuvchining parolini o'zgartirish
# def change_password():
#     current_password = input("Hozirgi parolingizni kiriting: ")
#     new_password = input("Yangi parolni kiriting: ")
#     confirm_password = input("Yangi parolni tasdiqlang: ")
    
#     if new_password == confirm_password:
#         print("Parol muvaffaqiyatli yangilandi.")
#     else:
#         print("Parollar mos kelmaydi. Iltimos, qaytadan urinib ko'ring.")

# # 5. To'liq foydalanuvchi ma'lumotlarini ko'rsatish
# def display_user_info(name, age):
#     print(f"\nFoydalanuvchi: {name}")
#     print(f"Yosh: {age}")
#     print(f"Tizimga kirishingiz mumkin.")

# # 6. Foydalanuvchidan tanlov olish
# def user_choice():
#     print("\nIltimos, tanlov qiling:")
#     print("1. Parolni yangilash")
#     print("2. Ma'lumotni ko'rish")
#     print("3. Chiqish")
    
#     choice = int(input("Tanlovni kiriting (1/2/3): "))
#     return choice

# # 7. Asosiy dastur
# def main():
#     name, age = get_user_info()
#     print(validate_user_age(age))
    
#     while True:
#         choice = user_choice()
        
#         if choice == 1:
#             change_password()
#         elif choice == 2:
#             display_user_info(name, age)
#         elif choice == 3:
#             print("Dasturdan chiqyapman...")
#             break
#         else:
#             print("Noto'g'ri tanlov. Iltimos, qayta urinib ko'ring.")

# # 8. Dastur ishga tushirish
# if __name__ == "__main__":
#     main()
