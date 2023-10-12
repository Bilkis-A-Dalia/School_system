from School import School,ClassRoom,Subject
from Persons import Student, Teacher

def main():
    school = School('Dalia', 'ctg')

    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine= ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    # add student
    abir = Student('Abir khan',eight)
    school.student_admission(abir)
    abira = Student('Abira khan',eight)
    school.student_admission(abira)
    abiri = Student('Abiri khan',eight)
    school.student_admission(abiri)

    # Add subjects
    bcom_teacher = Teacher('Rabbi')
    bcom = Subject('BCOM',bcom_teacher)
    eight.add_subject(bcom)

    bee_teacher = Teacher('Nadib')
    bee = Subject('BEE',bee_teacher)
    eight.add_subject(bee)

    # exam
    eight.take_semester_final()

    print(school)

if __name__ =='__main__':
    main()