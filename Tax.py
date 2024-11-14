def Tax(year_total_income, total_necessary_expenses):
    #입력값 총매출액(부가세포함) 필요경비(보험료, 재료비, 공과금, 배달수수료 등 사업에 필요한 모든 경비)

    vat = 0
    tax = 0


    ########################### 부가가치세 ##############################
    # 1년간 매출액 10400만원 이상 매출세액 - 매입세액
    if year_total_income >= 104000000:
        vat = year_total_income *0.1 - total_necessary_expenses *0.1
    # 1년간 매출액 10400만원 미만 매출액 * 15% * 10%- 공제세액(매입 * 0.5%)
    else:
        vat = year_total_income * 0.15 * 0.1 - total_necessary_expenses * 0.005



    ####################### 종합소득세 ########################
    income = year_total_income - (year_total_income*0.1) - total_necessary_expenses

    if income <= 12000000:  # 1,200만원 이하
        tax = income * 0.06
    elif income <= 46000000:  # 1,200만원 초과 ~ 5,000만원 이하
        tax = income * 0.15 - 1260000
    elif income <= 88000000:  # 5,000만원 초과 ~ 8,800만원 이하
        tax = income * 0.24 - 5760000
    elif income <= 150000000:  # 8,800만원 초과 ~ 1억 5천만원 이하
        tax = income * 0.35 - 15440000
    elif income <= 300000000:  # 1억 5천만원 초과 ~ 3억 이하
        tax = income * 0.38 - 19940000
    elif income <= 500000000:  # 3억 초과 ~ 5억 이하
        tax = income * 0.40 - 25940000
    elif income <= 1000000000:  # 5억 초과 ~ 10억 이하
        tax = income * 0.42 - 35940000
    else:   # 10억 초과
        tax = income * 0.45 - 65940000
    
    return vat + tax