Given a number, we need to prefix with $ sign and add 2 decimals points.
Example:
3 --> $3.00
4.2 --> $4.20

Use string formatting:
'${:.2f}'.format(amount) where amount is user input.
