import numpy as np
import pylab as pb

betaDif = 1e-2
tetaAtm = 0.01
nPorosity = 0.7
teta0 = nPorosity

n = 10
m = 5
t = 3600
l = 1
h = l / n
tau = t / m

tetaLst = {}


def key(i, k):
    return f"{i}|{k}"


def teta(i, k, val=None):
    if val == None:
        return tetaLst[key(i, k)]
    else:
        tetaLst[key(i, k)] = val


def D(th):
    return (1 - np.exp(-13 * th)) * (1e-6)


def a(i, k):
    return 0.5 * tau * (D(teta(i, k - 1)) + D(teta(i - 1, k - 1))) / h*h


def b(i, k):
    return 0.5 * tau * (D(teta(i + 1, k - 1)) + D(teta(i, k - 1))) / h*h


def c(i, k):
    return a(i, k) + b(i, k) + tau / h*h


def alpha(i, k):
    if i == 1:
        return D(teta(0, k - 1))(D(teta(0, k - 1)) - h * betaDif)
    else:
        return b(i - 1, k) / (c(i - 1, k) - alpha(i - 1, k) * a(i - 1, k))


def beta(i, k):
    if i == 1:
        return ((-h * betaDif * tetaAtm) / (D(teta(0, k - 1)) - h * betaDif))
    else:
        return ((a(i - 1, k) * beta(i - 1, k) + teta(i - 1, k - 1)) / (c(i - 1, k) - alpha(i - 1, k) * a(i - 1, k)))


for i in range(n + 1):
    teta(i, 0, teta0)

for k in range(1, m + 1):
    teta(n, k, beta(n, k) / (1 - alpha(n, k)))
    for i in range(n - 1, -1, -1):
        teta(i, k, alpha(i + 1, k) * teta(i + 1, k) + beta(i + 1, k))


def table():
    def s(n=1):
        return "" * n
    rows = []
    rows.append(["↓x t→", *[f"{i} | {i * tau}c" for i in range(m + 1)]])

    for i in range(n + 1):
        rows.append([f"{i} | {round(i * h, 3)}m"])
        rows[-1].extend([teta(i, k) for k in range(m + 1)])
        border = s(len(rows[0]) * 23 - m - 1)
        print(border)
        for row in rows:
            levelling = [str(i).center(23) for i in row[1:]]
            levelling.insert(0, row[0].center(10))
            print(s().join(levelling))
            print(border)


def plot():
    xList = [i * h for i in range(n + 1)]
    for k in range(1, m + 1):
        yList = [teta[x, k] for x in range(n + 1)]
        pb.plot(xList, yList)

        pb.title("Розподіл вологи в грунті")
        pb.xlabel('x')
        pb.ylabel('teta')
        pb.grid()
        pb.show()


table()
plot()
