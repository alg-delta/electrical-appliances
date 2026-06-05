# функція для ініціалізації бази даних та додавання даних
from app import app
from models import db, Sushi, Main, Dop, Main22, Main222
    
def create_db():
    with app.app_context():
        # db.drop_all() # видаляє всі таблиці (для навчання)
        db.create_all()  # створює заново

        if not Sushi.query.first():
            # ТИПИ СУШІ
            sushi1 = Sushi(name="б/у Техніка", description="Технікі яка пройшла перевірку і була відновлена до спрпаного технічного стану",
                                    image="images/images.jpg")
            sushi2 = Sushi(name="Нова техніка", description="",
                                    image="images/d8984b4523c28d08253ef367bce4.png.webp")
            sushi3 = Sushi(name="Аксесуари", description="Навушники, чохли, зарядні порти, блоки живлення, та інше",
                                     image="images/gg.webp")

            # Додаємо всі суші в чергу (session) БД
            db.session.add_all([sushi1, sushi2, sushi3])

        if not Main.query.first():
            # ГОЛОВНІ ІНГРЕДІЄНТИ
            main1 = Main(name="повербенк", price=24.0, image="images/01_PowerBank.jpg")
            main2 = Main(name="автомобільні тримачі", price=3.5, image="images/109745_005.jpg")
            main3 = Main(name="перевірка техніки", price=10.0, image="images/images.jpg")
            main4 = Main(name="ремонт", price=12.5, image="images/unnamed.webp")
            main5 = Main(name="захисні плівки", price=3.0, image="images/6454697090_w640_h320_zaschitnaya-plenka-dlya.webp")
            main6 = Main(name="захисне скло", price=8.5, image="images/fb1f749a-ab96-11ed-8262-ac162d75ecbb_thumbnail_min.jpg")
            main7 = Main(name="чохли", price=8.0, image="images/dbd95ab847bf39bdfd42b92175a5767c.webp")
            main8 = Main(name="блок живлення", price=8.0, image="images/321621434.webp")
            main9 = Main(name="зарядний порт", price=6.0, image="images/images.png")
        if not Main22.query.first():
            main10 = Main22(name="samsung s22 ultra смартфон 12/256 гб", price=660.0, image="images/5389163415573119.webp")
            main11 = Main22(name="redmi not 15 смартфон 8/126гб", price=250.0, image="images/p7_blue_backleft_result_2.webp")
            main12 = Main22(name="poco x7 pro 8/256", price=270.0, image="images/o10-yellow-backright45_result_1_1.webp")
            main13 = Main22(name="смартфон 8/256", price=200.0, image="images/d8984b4523c28d08253ef367bce4.png.webp")
        if not Main222.query.first():
            main14 = Main222(name="бу samsung s22 ultra смартфон 12/256 гб", price=460.0, image="images/5389163415573119.webp")
            main15 = Main222(name="бу poco x7 pro 8/256", price=220.0, image="images/o10-yellow-backright45_result_1_1.webp")

            # Додаємо всі головні інгредієнти в чергу (session) БД
            db.session.add_all([main1, main2, main3, main4, main5, main6, main7, main8, main9, main10, main11, main12, main13, main14, main15])

        if not Dop.query.first():
            # ДОПОВНЕННЯ
            dop1 = Dop(name="В кредит", price=0, image="images/ginger.jpg")
            dop2 = Dop(name="Оплата при отриманні", price=0, image="images/wasabi.jpg")
            dop3 = Dop(name="Самовивіз", price=0, image="images/soy_sauce.jpg")
            dop4 = Dop(name="Передплата", price=0, image="images/chopsticks.jpg")

            # Додаємо всі доповнення в чергу (session) БД
            db.session.add_all([dop1, dop2, dop3, dop4])


        # Зберігаємо всі зміни з черги (сесії) у БД
        db.session.commit()

if __name__ == '__main__':
    create_db()
    print("Базу даних успішно ініціалізовано!")