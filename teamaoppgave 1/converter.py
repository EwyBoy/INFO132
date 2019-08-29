# coding=utf-8
EUR = 9.99
USD = 8.98


def convert(nok, currency):
    return str(round(nok / currency, 2))


def main():
    nok = input('NOK: ')
    print str(nok) + ' kroner tilsvarer ' + str(convert(nok, EUR)) + ' Euro og ' + str(convert(nok, USD)) + ' Dollar'
    print 'NOK ' + str(nok) + ' tilsvarer ' + str(convert(nok, EUR) + '€' + ' og ' + str(convert(nok, USD)) + '$')


if __name__ == '__main__':
    main()
