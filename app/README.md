# Database Design

db = {
    course_id: {
    assignments: {
        assignment_id:{
        assignment_name: STRING, 
        assignment_sum: INT,
        assignment_submission_amount: INT,
        },
        assignment_id2:{
        ...
        },
        ...
    },
    students: {
        student_id: {
        submissions: {
            assignment_id: {
            grade: INT
            },
            assignment_id2: {
            ...
            },
            ...
        },
        student_sum: INT, 
        student_submission_amount: INT
        }, 
        student_id2: {
        ...
        },
    }
    }, 
    course_id2: {
    ...
    }, 
    ...
}

