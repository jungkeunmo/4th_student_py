
DB_STUDENT = [
    {
        "name": "홍도기",
        "age": "16"
    },
    {
        "name": "김우진",
        "age": "15"
    }
]

def students():
    print("-----------------")
    print("1. student list")
    print("2. create student")
    print("3. delete student")
    print("4. exit program")
    print("-----------------")

    answer = int(input(">>"))

    if answer == 1:
        view_student()
    elif answer == 2:
        create_student()
    elif answer == 3:
        delete_student()
    elif answer == 4:
        print("프로그램 종료")
    else:
        print("잘못 입력하셨습니다")    
        students()

def view_student():
    print("👋 STUDENT LIST 👋")
    for student in DB_STUDENT:
        print(f"학생 이름 : {student['name']}")
        print(f"학생 나이 : {student['age']}")
        print("--------------------------")
    students()
    

def create_student():
    input_name = input("학생 이름을 입력해주세요. >>")
    input_age = input("학생 나이를 입력해주세요. >>")

    push_data = {
        "name": input_name,
        "age": input_age
    }

    DB_STUDENT.append(push_data)

    students()

def delete_student():
    for student in enumerate(DB_STUDENT):
        print(f"{student[0]} _ {student[1]['name']}")

    input_index = int(input("삭제할 학생의 번호를 입력해주세요 >>"))

    DB_STUDENT.pop(input_index)
    print("입력하신 학생이 삭제되었습니다.")
    students()

students()
