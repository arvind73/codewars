Man wants to buy a car worth $8000, while he has old car worth $2000 and keeps the old one until he buys the new one. He saves $1000 but the prices of his old car and new
one decrease of 1.5 percent per month. Furthermore this percent of loss increases of 0.5 percent at the end of every two months.

function has four arguments namely startPriceOld(old car), startPriceNew(new car), savingperMonth(1000), percentLossByMonth(1.5).
Here percentLossByMonth reduces to 0.5 at end of every 2 monnths. Our output have have amount of mounts he takes to save up money i.e., $8000 and also the amount left over money he
has after buying it(rounded off value).


Check condition if price of new car is greater than sum of old car and the savings. If no, then increment months and savings per month.
while startPriceOld + savings < startPriceNew:
        months += 1
        savings += savingperMonth      
        
Initialize months and savings to 0.
Use logic to raise percentLoss if its a second month
if months % 2 == 0:
            percentLossByMonth += 0.5 # data
            
Initialize startPriceOld and startPriceNew

        startPriceOld *= ((100 - percentLossByMonth) / 100)
        startPriceNew *= ((100 - percentLossByMonth) / 100)
        
This is done since for every month, the cars values will be depreciated.
Now check left over money: (startPriceOld + savings - startPriceNew) and round it up using round() function.
Finally output the months and left over money as the output.

            
