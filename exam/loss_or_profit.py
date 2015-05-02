def loss_or_profit(income,outcome):
    result_income = 0
    result_outcome = 0
    result = 0
    
    for x in income:
        result_income += x

    for y in outcome:
        result_outcome += y
    result = result_income - result_outcome
    if result > 0:
        result = "+" + str(result)
    elif result < 0:
        result =  str(result)
    else :
        result = "=" + str(result)


    return result
