from dotenv import load_dotenv

load_dotenv()

from app import app, db
from app.models import Employee


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    db.session.add(employee)

    # explanation of getter/setter
    # employee.password => goes thru logic of @property password in the models.py file
    # changing employee.password => goes thru logic of @password.setter password in the models.py file


    employee2 = Employee(name="Tyler", employee_number=1235, password="password")
    db.session.add(employee2)

    db.session.commit()
