def tribonacci(signature,n):
    tribonacci = []

    for i in range(n):
        new_elm = signature[-1] + signature[-2] + signature[-3]
        signature.append(new_elm)
        elm = signature.pop(0)
        tribonacci.append(elm)

    return tribonacci

def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res

def tribonacci(signature,n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))

    return signature[:n]

def tribonacci(signature,n):
    res = signature
    while len(res) < n:
        res.append(sum(res[-3:]))
    return res[:n]


Test.assert_equals(tribonacci([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])
