def gradingStudents(grades):
    array = []
    for grade in grades :
        # rounds grade to  nearest 5th
        # use float for percision
        roundedGrade = int(round(grade/5.0)*5.0) 
        if roundedGrade > grade and roundedGrade >= 40:
            array.append(roundedGrade)
        else:
            array.append(grade)
    return array