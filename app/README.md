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

# code practice/design choice

1. Use early returns instead of long if statements to ensure future extensiability of code. (for example, if more filters are needed in the future before processing a request)
2. Try to keep time complexity low when retrieving information, it's fine to shift complexity to addition of information. Sacrificing a bit of space complexity is fine. 

