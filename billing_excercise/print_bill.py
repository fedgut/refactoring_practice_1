import locale
import math

def statement(invoice, plays):
    totalAmount = 0
    volumeCredits = 0
    result = "statement for {client}\n".format(client=invoice.customer)

    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    for perf in invoice.performances:
        play = plays[perf.playID]
        thisAmmount = 0

        if play.type == "tragedy":
            thisAmmount = 40000
            if perf.audience > 30:
                thisAmmount += 1000 * (perf.audience - 30)
        elif play.type == "comedy":
            thisAmmount = 30000
            if (perf.audience > 20) :
                thisAmmount += 10000 + 500 * (perf.audience - 20)
                thisAmmount += 300 * perf.audience
        else:
            raise TypeError("Unknown play type {play}".format(play=play.type))

        # add volume credits
        volumeCredits += max(perf.audience - 30, 0)

        # add extra credit for every ten comedy attendees
        if ("comedy" == play.type):
            volumeCredits += math.floor(perf.audience / 5)

        #   print line for this order
        result += ' {0}: {2} ({1} seats)\n'.format(play.name, perf.audience, locale.currency(thisAmmount/100))
        totalAmount += thisAmmount

    result += "ammount owed is {}\n".format(locale.currency(totalAmount/100))
    result += "you earned {} credits".format(volumeCredits)
    print(result)
