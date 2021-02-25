def solution(new_id):
    new_id = new_id.lower() # 1단계
    
    answer = ''    # 2단계
    for char in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += char
    
    while '..' in answer:
        answer = answer.replace('..', '.')
        
    if answer[0] == '.':
        answer = answer[1:] if answer != '.' else '.'
            
    if answer[-1] == '.':
        answer = answer[:-1]
        
    if answer == '':
        answer = 'a'
    
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
            
    if len(answer) < 3:
        answer = answer + (answer[-1] * (3 - len(answer))) 
    return answer
