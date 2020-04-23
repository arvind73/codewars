
#1
def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    months = 0
    savings = 0

    while startPriceOld + savings < startPriceNew:
        months += 1
        savings += savingperMonth

        # Raise the percentLoss if this is the second month.
        if months % 2 == 0:
            percentLossByMonth += 0.5
            print('this is the month: ', months)

        startPriceOld *= ((100 - percentLossByMonth) / 100)
        startPriceNew *= ((100 - percentLossByMonth) / 100)

    return [months, round(startPriceOld + savings - startPriceNew)]

#2
def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    i = 0
    while savingperMonth * i + startPriceOld < startPriceNew:
        if i % 2:
            percentLossByMonth += 0.5
        startPriceOld -= startPriceOld * 0.01 * percentLossByMonth
        startPriceNew -= startPriceNew * 0.01 * percentLossByMonth
        i += 1
    return [i, round(savingperMonth * i + startPriceOld - startPriceNew)]

#test.assert_equals(nbMonths(2000, 8000, 1000, 1.5), [6, 766])
